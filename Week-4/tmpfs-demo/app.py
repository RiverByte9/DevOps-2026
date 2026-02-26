import os
from flask import Flask, request, jsonify, render_template_string
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# ─────────────────────────────────────────────
# 🔐 Load credentials from tmpfs secret files
#    These files live in memory only (tmpfs).
#    Nothing is written to disk.
# ─────────────────────────────────────────────
def read_secret(name: str) -> str:
    """Read a secret from the tmpfs-mounted /run/secrets/ directory."""
    secret_path = f"/run/secrets/{name}"
    try:
        with open(secret_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        # Fallback to env var for local development without Docker
        return os.environ.get(name.upper(), "")

DB_HOST     = os.environ.get("DB_HOST", "db")
DB_PORT     = os.environ.get("DB_PORT", "5432")
DB_NAME     = read_secret("db_name")
DB_USER     = read_secret("db_user")
DB_PASSWORD = read_secret("db_password")


def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def init_db():
    """Create the todos table if it doesn't exist."""
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id      SERIAL PRIMARY KEY,
                    task    TEXT    NOT NULL,
                    done    BOOLEAN NOT NULL DEFAULT FALSE,
                    created TIMESTAMPTZ DEFAULT NOW()
                )
            """)
        conn.commit()


# ─── HTML Template ───────────────────────────

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>tmpfs Todo</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;500&display=swap');

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg: #0d0d0d;
      --surface: #161616;
      --border: #2a2a2a;
      --green: #00ff88;
      --dim: #444;
      --text: #e8e8e8;
      --muted: #666;
    }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'IBM Plex Sans', sans-serif;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      padding: 60px 16px;
    }

    .container { width: 100%; max-width: 560px; }

    header {
      margin-bottom: 40px;
    }

    .badge {
      display: inline-block;
      font-family: 'IBM Plex Mono', monospace;
      font-size: 10px;
      color: var(--green);
      border: 1px solid var(--green);
      padding: 2px 8px;
      border-radius: 2px;
      letter-spacing: 0.1em;
      margin-bottom: 12px;
      opacity: 0.8;
    }

    h1 {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 28px;
      font-weight: 600;
      letter-spacing: -0.02em;
    }

    .subtitle {
      margin-top: 6px;
      font-size: 13px;
      color: var(--muted);
      font-weight: 300;
    }

    .input-row {
      display: flex;
      gap: 8px;
      margin-bottom: 32px;
    }

    input[type="text"] {
      flex: 1;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 12px 16px;
      font-family: 'IBM Plex Sans', sans-serif;
      font-size: 14px;
      border-radius: 4px;
      outline: none;
      transition: border-color 0.15s;
    }
    input[type="text"]:focus { border-color: var(--green); }
    input[type="text"]::placeholder { color: var(--dim); }

    button {
      background: var(--green);
      color: #000;
      border: none;
      padding: 12px 20px;
      font-family: 'IBM Plex Mono', monospace;
      font-size: 13px;
      font-weight: 600;
      border-radius: 4px;
      cursor: pointer;
      white-space: nowrap;
      transition: opacity 0.15s;
    }
    button:hover { opacity: 0.85; }

    .section-label {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 10px;
      letter-spacing: 0.12em;
      color: var(--muted);
      text-transform: uppercase;
      margin-bottom: 12px;
    }

    .todo-list { list-style: none; }

    .todo-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 14px 16px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 4px;
      margin-bottom: 8px;
      transition: border-color 0.15s;
    }
    .todo-item:hover { border-color: #3a3a3a; }
    .todo-item.done { opacity: 0.45; }

    .todo-item input[type="checkbox"] {
      appearance: none;
      width: 16px;
      height: 16px;
      border: 1px solid var(--dim);
      border-radius: 2px;
      cursor: pointer;
      flex-shrink: 0;
      position: relative;
      transition: all 0.15s;
    }
    .todo-item input[type="checkbox"]:checked {
      background: var(--green);
      border-color: var(--green);
    }
    .todo-item input[type="checkbox"]:checked::after {
      content: '';
      position: absolute;
      left: 4px; top: 1px;
      width: 5px; height: 9px;
      border: 2px solid #000;
      border-top: none; border-left: none;
      transform: rotate(45deg);
    }

    .task-text {
      flex: 1;
      font-size: 14px;
      font-weight: 300;
      line-height: 1.4;
    }
    .done .task-text { text-decoration: line-through; }

    .delete-btn {
      background: none;
      color: var(--dim);
      padding: 4px 6px;
      font-size: 16px;
      font-weight: 400;
      border-radius: 2px;
      transition: color 0.15s;
    }
    .delete-btn:hover { color: #ff4d4d; background: none; }

    .empty {
      text-align: center;
      padding: 40px 0;
      color: var(--muted);
      font-family: 'IBM Plex Mono', monospace;
      font-size: 12px;
      border: 1px dashed var(--border);
      border-radius: 4px;
    }

    .security-note {
      margin-top: 48px;
      padding: 16px;
      border: 1px solid #1e3a2e;
      border-radius: 4px;
      background: #0a1f15;
    }
    .security-note h3 {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 11px;
      color: var(--green);
      letter-spacing: 0.1em;
      margin-bottom: 8px;
    }
    .security-note p {
      font-size: 12px;
      color: var(--muted);
      line-height: 1.6;
      font-weight: 300;
    }
    code {
      font-family: 'IBM Plex Mono', monospace;
      color: var(--green);
      font-size: 11px;
    }
  </style>
</head>
<body>
<div class="container">
  <header>
    <div class="badge">🔐 TMPFS SECURED</div>
    <h1>todo.</h1>
    <p class="subtitle">Credentials loaded from in-memory tmpfs — never touching disk.</p>
  </header>

  <div class="input-row">
    <input type="text" id="taskInput" placeholder="What needs doing?" />
    <button onclick="addTodo()">+ Add</button>
  </div>

  <p class="section-label">Tasks</p>
  <ul class="todo-list" id="todoList">
    {% if todos %}
      {% for t in todos %}
      <li class="todo-item {{ 'done' if t.done }}" id="item-{{ t.id }}">
        <input type="checkbox" {{ 'checked' if t.done }}
               onchange="toggleTodo({{ t.id }}, this.checked)">
        <span class="task-text">{{ t.task }}</span>
        <button class="delete-btn" onclick="deleteTodo({{ t.id }})">×</button>
      </li>
      {% endfor %}
    {% else %}
      <li class="empty">no tasks yet — add one above</li>
    {% endif %}
  </ul>

  <div class="security-note">
    <h3>// HOW CREDENTIALS ARE LOADED</h3>
    <p>
      Secrets live in <code>/run/secrets/</code> — a <code>tmpfs</code> mount.
      They exist only in RAM. No <code>docker inspect</code>, no disk forensics,
      no shell history leaks them. When the container stops, they vanish.
    </p>
  </div>
</div>

<script>
  async function addTodo() {
    const input = document.getElementById('taskInput');
    const task = input.value.trim();
    if (!task) return;
    await fetch('/todos', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ task })
    });
    input.value = '';
    location.reload();
  }

  document.getElementById('taskInput').addEventListener('keydown', e => {
    if (e.key === 'Enter') addTodo();
  });

  async function toggleTodo(id, done) {
    await fetch(`/todos/${id}`, {
      method: 'PATCH',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ done })
    });
    document.getElementById(`item-${id}`).classList.toggle('done', done);
  }

  async function deleteTodo(id) {
    await fetch(`/todos/${id}`, { method: 'DELETE' });
    document.getElementById(`item-${id}`).remove();
  }
</script>
</body>
</html>
"""


# ─── Routes ──────────────────────────────────

@app.route("/")
def index():
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id, task, done FROM todos ORDER BY created DESC")
            todos = cur.fetchall()
    return render_template_string(TEMPLATE, todos=todos)


@app.route("/todos", methods=["POST"])
def create_todo():
    task = request.json.get("task", "").strip()
    if not task:
        return jsonify({"error": "task is required"}), 400
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO todos (task) VALUES (%s) RETURNING id", (task,))
            new_id = cur.fetchone()[0]
        conn.commit()
    return jsonify({"id": new_id, "task": task, "done": False}), 201


@app.route("/todos/<int:todo_id>", methods=["PATCH"])
def update_todo(todo_id):
    done = request.json.get("done")
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE todos SET done=%s WHERE id=%s", (done, todo_id))
        conn.commit()
    return jsonify({"id": todo_id, "done": done})


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM todos WHERE id=%s", (todo_id,))
        conn.commit()
    return jsonify({"deleted": todo_id})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)