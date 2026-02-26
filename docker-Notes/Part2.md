# 🐳 Docker Core Concepts — Beginner's Guide

> Based on thenewboston's Docker Tutorial Series (Tutorial 2)

---

## Overview

Docker is a tool that lets you package and run applications in isolated, portable environments — solving the classic _"it works on my machine"_ problem.

Three core building blocks make it all work:

| Concept | Analogy | Role |
|---|---|---|
| **Image** | Recipe card / Blueprint | Read-only template with everything needed to run an app |
| **Container** | Baked cake / Running instance | A live copy created from an image |
| **Docker Daemon** | Chef / Engine | Background process that does all the actual work |

---

## Core Concepts

### 🖼️ Image — The Blueprint

An image is a **read-only template** containing the OS base, app code, libraries, config files, and environment variables needed to run your application.

- Images are **immutable** — you can't change them once built
- To make changes, you build a **new** image
- Images are stored/cached locally on disk after the first pull

**Example:** The `hello-world` image is a tiny official test image that just prints a message and exits.

---

### 📦 Container — The Running Instance

A container is a **live, runnable copy** made from an image.

- Each container runs in its own isolated environment (filesystem, memory, network, processes)
- You can run **many containers from a single image** — each independent
- Much lighter than full virtual machines — they share the host machine's kernel

---

### ⚙️ Docker Daemon — The Engine

When you install Docker, you get two pieces:

- **Docker CLI** — the command-line tool you type into (`docker run`, `docker ps`, etc.). This is your remote control.
- **Docker Daemon** — the background process that actually builds images, runs containers, talks to Docker Hub, and manages storage and networking.

That's why `docker version` shows both a **Client** and **Server** version — they're separate components.

---

## What Happens When You Run `docker run hello-world`

```
$ docker run hello-world
```

Here's the step-by-step flow:

1. You type the command → **CLI receives the order**
2. CLI tells the daemon: _"Run the hello-world image in a new container"_
3. Daemon checks locally: _"Do I have this image cached?"_
   - **First time:** No → _"Unable to find image 'hello-world:latest' locally"_
   - Daemon contacts **Docker Hub** (public image registry)
   - Downloads the image (pulls layers)
4. Daemon uses the image to **create and start a fresh container**
5. Container runs its program → prints the message → exits
6. Output is sent back to the CLI → you see it on screen

**Second time you run the same command:**
- Daemon finds the cached image locally → **no download needed**
- Instantly creates a new container from the local copy ⚡

---

## Quick Command Reference

| Command | What it does |
|---|---|
| `docker pull <image>` | Download an image from Docker Hub |
| `docker run <image>` | Create and start a container from an image |
| `docker ps` | List currently running containers |
| `docker ps -a` | List all containers (including stopped ones) |
| `docker images` | List all locally cached images |

---

## Mental Model Summary

```
Docker Hub (store)
      |
      | docker pull
      ↓
   [Image]          ← Recipe card (read-only, stored on disk)
      |
      | docker run (x many times)
      ↓
[Container 1]  [Container 2]  [Container 3]   ← Baked cakes (running in memory)

All managed by the Docker Daemon (the chef) behind the scenes.
```

---

## Key Takeaways

- **Image** = the frozen blueprint. One template, many possible containers.
- **Container** = a running instance of an image. Isolated, lightweight, temporary.
- **Docker Daemon** = the real engine. The CLI just sends it instructions.
- **Caching** = images are saved locally after the first pull, making subsequent runs instant.

---

*This covers Tutorial 2 — conceptual foundations. Next tutorials dive into actual commands and building your own images.*