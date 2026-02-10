from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kajal | AWS DevOps Engineer</title>

<style>
/* ===== GLOBAL ===== */
* { margin:0; padding:0; box-sizing:border-box; }

:root {
  --bg-primary:#ffffff;
  --bg-secondary:#f8f9fa;
  --bg-card:#ffffff;
  --text-primary:#1a1a1a;
  --text-secondary:#666;
  --accent:#FF9900;
  --border:#e0e0e0;
  --shadow:rgba(0,0,0,.1);
}

[data-theme="dark"] {
  --bg-primary:#0f1419;
  --bg-secondary:#1a1f2e;
  --bg-card:#232940;
  --text-primary:#e6e6e6;
  --text-secondary:#aaa;
  --border:#2d3748;
  --shadow:rgba(0,0,0,.3);
}

body {
  font-family:system-ui, sans-serif;
  background:var(--bg-primary);
  color:var(--text-primary);
}

/* ===== NAV ===== */
nav {
  background:var(--bg-card);
  box-shadow:0 2px 10px var(--shadow);
  position:sticky; top:0;
}

.nav-container {
  max-width:1200px;
  margin:auto;
  padding:1rem 2rem;
  display:flex;
  justify-content:space-between;
}

.logo { color:var(--accent); font-weight:700; font-size:1.4rem; }

.nav-links { display:flex; gap:1.5rem; list-style:none; }
.nav-links a { color:var(--text-primary); text-decoration:none; }

/* ===== HERO ===== */
.hero {
  padding:6rem 2rem;
  text-align:center;
  background:linear-gradient(135deg,var(--bg-secondary),var(--bg-card));
}

.hero h1 { font-size:3rem; }
.tagline { color:var(--accent); font-size:1.4rem; margin:1rem 0; }
.subtitle { color:var(--text-secondary); }

/* ===== SECTIONS ===== */
.container {
  max-width:1200px;
  margin:auto;
  padding:4rem 2rem;
}

.section-title {
  text-align:center;
  margin-bottom:3rem;
}
.section-title h2 { font-size:2.4rem; }
.underline {
  width:70px;
  height:4px;
  background:var(--accent);
  margin:1rem auto;
}

/* ===== PROJECTS ===== */
.projects-grid {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
  gap:2rem;
}

.project-card {
  background:var(--bg-card);
  border-radius:12px;
  box-shadow:0 4px 8px var(--shadow);
  transition:.3s;
}
.project-card:hover { transform:translateY(-6px); }

.project-header {
  padding:1.5rem;
  background:linear-gradient(135deg,var(--accent),#cc7a00);
  color:white;
}

.project-body { padding:1.5rem; }

.project-description {
  color:var(--text-secondary);
  margin-bottom:1rem;
}

.tech-stack {
  display:flex;
  flex-wrap:wrap;
  gap:.5rem;
}

.tech-badge {
  background:var(--bg-secondary);
  padding:.3rem .8rem;
  border-radius:4px;
  font-size:.85rem;
}

.project-links {
  margin-top:1rem;
}
.project-link {
  display:block;
  text-align:center;
  padding:.6rem;
  background:var(--bg-secondary);
  text-decoration:none;
  border-radius:6px;
  color:var(--text-primary);
}
.project-link:hover {
  background:var(--accent);
  color:white;
}

/* ===== FOOTER ===== */
footer {
  text-align:center;
  padding:2rem;
  color:var(--text-secondary);
}
</style>
</head>

<body>

<nav>
  <div class="nav-container">
    <div class="logo">$kajal</div>
    <ul class="nav-links">
      <li><a href="#projects">Projects</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </div>
</nav>

<section class="hero">
  <h1>Hi, I'm Kajal</h1>
  <p class="tagline">AWS DevOps Engineer</p>
  <p class="subtitle">Building scalable cloud infrastructure and automating workflows.</p>
</section>

<section id="projects" class="container">
<div class="section-title">
  <h2>Featured Projects</h2>
  <div class="underline"></div>
</div>

<div class="projects-grid">

<!-- PROJECT 1 -->
<div class="project-card">
  <div class="project-header">
    <h3>Multi-Container Docker Compose</h3>
    <p>Containerization</p>
  </div>
  <div class="project-body">
    <p class="project-description">
      Built and managed a multi-container application using Docker Compose with service networking and environment isolation.
    </p>
    <div class="tech-stack">
      <span class="tech-badge">Docker</span>
      <span class="tech-badge">Docker Compose</span>
      <span class="tech-badge">Linux</span>
    </div>
    <div class="project-links">
      <a href="#" class="project-link">GitHub</a>
    </div>
  </div>
</div>

<!-- PROJECT 2 -->
<div class="project-card">
  <div class="project-header">
    <h3>Containerized Flask App on AWS ECS</h3>
    <p>Cloud & Containers</p>
  </div>
  <div class="project-body">
    <p class="project-description">
      Deployed a Dockerized Flask application on AWS ECS with ALB, IAM roles, and scalable task definitions.
    </p>
    <div class="tech-stack">
      <span class="tech-badge">AWS ECS</span>
      <span class="tech-badge">Docker</span>
      <span class="tech-badge">Flask</span>
      <span class="tech-badge">ALB</span>
    </div>
    <div class="project-links">
      <a href="#" class="project-link">GitHub</a>
    </div>
  </div>
</div>

<!-- PROJECT 3 -->
<div class="project-card">
  <div class="project-header">
    <h3>AWS ECS Infrastructure with Terraform</h3>
    <p>Infrastructure as Code</p>
  </div>
  <div class="project-body">
    <p class="project-description">
      Provisioned complete ECS infrastructure using Terraform with modular design and remote state management.
    </p>
    <div class="tech-stack">
      <span class="tech-badge">Terraform</span>
      <span class="tech-badge">AWS</span>
      <span class="tech-badge">ECS</span>
      <span class="tech-badge">VPC</span>
    </div>
    <div class="project-links">
      <a href="#" class="project-link">GitHub</a>
    </div>
  </div>
</div>

</div>
</section>

<footer>
  © 2026 Kajal | DevOps Portfolio
</footer>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
