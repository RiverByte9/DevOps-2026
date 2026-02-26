# tmpfs-demo — Secure credentials with Docker tmpfs secrets

A minimal Flask to-do app that demonstrates loading database credentials
from Docker's tmpfs-backed secrets, instead of environment variables.

The data flow — how a secret goes from file → RAM → app

Host disk: ./secrets/db_password.txt
           ↓  (Docker reads at startup)
tmpfs RAM: /run/secrets/db_password   ← inside container, in memory only
           ↓  (app.py reads at boot)
Variable:  DB_PASSWORD = "s3cr3tpassword!"


```
tmpfs-demo/
├── app.py               ← Flask app; reads creds from /run/secrets/
├── requirements.txt
├── Dockerfile           ← Multi-stage build, non-root user
├── docker-compose.yml   ← Wires up secrets → tmpfs mounts
├── setup-secrets.sh     ← Creates ./secrets/*.txt on the host
└── secrets/             ← ⚠️  Never commit this directory!
    ├── db_name.txt
    ├── db_user.txt
    └── db_password.txt
```

---

## Why tmpfs instead of env vars?

| | `environment: DB_PASSWORD=x` | tmpfs secret |
|---|---|---|
| Visible in `docker inspect` | ✅ yes (leak!) | ❌ no |
| Written to image layer | ✅ possibly | ❌ never |
| Survives container stop | ✅ yes | ❌ gone |
| Shell history exposure | ✅ yes | ❌ no |
| Accessible as a file in RAM | — | ✅ yes |

---

## How it works — step by step

1. **Host seed files** (`./secrets/*.txt`)  
   Plain text files on your machine. Docker reads them at startup.

2. **`secrets:` top-level key in compose**  
   Declares each secret and points to its seed file.

3. **Per-service `secrets:` list**  
   Tells Docker which services get which secrets injected.

4. **Docker mounts tmpfs**  
   For each secret, Docker creates an in-memory file at  
   `/run/secrets/<secret_name>` inside the container.  
   No disk I/O. No image layer. Just RAM.

5. **`app.py` reads the file**
   ```python
   def read_secret(name):
       with open(f"/run/secrets/{name}") as f:
           return f.read().strip()

   DB_PASSWORD = read_secret("db_password")
   ```

6. **Container stops → tmpfs destroyed**  
   The credentials are gone. Nothing to forensically recover.

---

## Quick start

```bash
# 1. Create secret files (run once)
bash setup-secrets.sh

# 2. Add secrets/ to .gitignore
echo "secrets/" >> .gitignore

# 3. Start everything
docker compose up --build

# 4. Open the app
open http://localhost:5000
```

---

## Prove it works — see tmpfs in action

```bash
# Shell into the running app container
docker compose exec app sh

# See the in-memory secret files
cat /run/secrets/db_password    # prints: s3cr3tpassword!

# Confirm it's tmpfs (not a real disk mount)
mount | grep secrets
# → tmpfs on /run/secrets type tmpfs (ro,nosuid,nodev,noexec,...)

# Now check docker inspect — credentials NOT visible
docker inspect tmpfs-demo-app-1 | grep -i password
# → (nothing)
```

---

## .gitignore reminder

```
secrets/
*.env
```

The `./secrets/` files are the ONE place credentials touch disk (your host).
In production, use a secrets manager (AWS Secrets Manager, Vault, GCP Secret Manager)
that injects directly into tmpfs without ever touching your filesystem.