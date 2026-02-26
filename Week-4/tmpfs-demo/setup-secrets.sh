#!/usr/bin/env bash
# setup-secrets.sh — run this once before `docker compose up`
# Creates the host-side seed files that Docker reads to populate tmpfs.

set -euo pipefail

mkdir -p secrets

echo -n "tododb"           > secrets/db_name.txt
echo -n "todouser"         > secrets/db_user.txt
echo -n "s3cr3tpassword!"  > secrets/db_password.txt

# Lock down permissions — only owner can read
chmod 600 secrets/*.txt

echo "✅  Secret files created in ./secrets/"
echo "    Add secrets/ to your .gitignore — never commit these!"