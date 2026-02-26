# 🐳 Docker Default Commands — Beginner's Guide

> Based on thenewboston's Docker Tutorial Series (Tutorial 3)  
> Prerequisites: [Tutorial 2 — Images, Containers & the Docker Daemon](./README.md)

---

## Core Concept: The Default Command

Every Docker image comes with a built-in **default command** — a pre-written instruction that says:

> _"When a container starts from this image, automatically run THIS program."_

Think of it like a note taped to a computer that says **"When you power on, do this."**

- Some images have a useful default (e.g., `hello-world` prints a message)
- Others have no default → the container starts and **immediately exits** because there's nothing to do
- You can always **override** the default by passing your own command

---

## Key Examples

### 1. `hello-world` — Has a default command

```bash
docker run hello-world
```

- Default: runs a tiny program that prints "Hello from Docker!" then exits
- Container lives for only a few seconds
- **Mental model:** An alarm clock set to _"play message → turn off."_ Wakes up, speaks, sleeps forever.

---

### 2. `busybox` — No default command

```bash
docker run busybox
```

- Busybox is a small (~5MB) Linux toolkit with basic commands (`ls`, `echo`, `cat`, etc.)
- But it has **no default command set**
- Result: container starts → finds nothing to do → **exits instantly with no output**
- **Mental model:** A new phone with no apps and no home screen. It boots, sits there, shuts down.

---

### 3. Overriding the Default Command

Add your command **after the image name** to override the default:

```bash
# List files in the container's root directory
docker run busybox ls

# Print a message
docker run busybox echo "hello"

# Detailed listing of /etc
docker run busybox ls -l /etc

# Keep container running (runs until you stop it)
docker run busybox sleep 1000
```

**Mental model:** Handing someone a phone and saying _"Don't do your normal startup — just open the camera right now."_

---

## The Full Flow (Step by Step)

When you run `docker run <image> [command]`, Docker:

1. Creates a new container from the image
2. Looks at the image's built-in default command
3. Runs that command automatically — **or** runs whatever you typed after the image name
4. When the command finishes, the container stops

```
docker run hello-world       → uses default   → prints message → exits
docker run busybox           → no default      → exits instantly
docker run busybox ls        → overrides       → lists files    → exits
docker run busybox sleep 1000 → overrides      → runs forever until stopped
```

---

## Old vs. New CLI Syntax

Docker introduced a more explicit subcommand style. Both work — the newer form is recommended:

| Old (still works) | New (recommended) |
|---|---|
| `docker run <image>` | `docker container run <image>` |
| `docker ps` | `docker container ls` |

The `container` subcommand makes it clear what you're operating on, as Docker expanded to manage networks, volumes, images, and more.

---

## Why Busybox for Learning?

Many real app images (`nginx`, `python`, `node`) are stripped down and **don't include** basic shell tools like `ls` or `echo`. Busybox packs all those basics into ~5MB — perfect for quick experiments without bloating your setup.

---

## Why Default Commands Matter

This concept is the foundation of almost everything in Docker:

| Image | Default Command | What it does |
|---|---|---|
| `nginx` | `nginx -g 'daemon off;'` | Starts serving on port 80 |
| `postgres` | `docker-entrypoint.sh postgres` | Starts the database server |
| `hello-world` | `/hello` | Prints a message and exits |
| `busybox` | _(none)_ | Exits immediately |
| Your app | `node app.js` or `python main.py` | Runs your application |

When you want to **explore inside a container interactively**, you'll override the default with `sh` or `bash` — covered in later tutorials.

---

## Quick Reference

```bash
# Run with default command
docker run <image>

# Override the default command
docker run <image> <command>

# Modern syntax (recommended)
docker container run <image> <command>

# Examples
docker run busybox ls
docker run busybox echo "hello world"
docker run busybox sleep 1000
```

---

*Tutorial 3 complete — you now understand default commands and how to override them. Next up: interactive containers with `sh`/`bash`.*