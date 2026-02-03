#!/bin/bash
# Show system environment and create custom project environment
echo "=== System Environment ==="
echo "User: $USER"
echo "Home: $HOME"
echo "Shell: $SHELL"
echo ""
# Count PATH directories
IFS=: read -ra paths <<< "$PATH"
echo "PATH has ${#paths[@]} directories"
# Create project environment with defaults
export PROJECT_NAME="${PROJECT_NAME:-MyApp}"
export PROJECT_ENV="${PROJECT_ENV:-development}"
export PROJECT_PORT="${PROJECT_PORT:-8080}"
echo ""
echo "=== Project Environment ==="
echo "Name: $PROJECT_NAME"
echo "Environment: $PROJECT_ENV"
echo "Port: $PROJECT_PORT"
# Save to file
cat > .env <<EOF
PROJECT_NAME=$PROJECT_NAME
PROJECT_ENV=$PROJECT_ENV
PROJECT_PORT=$PROJECT_PORT
EOF
echo ""
echo "Configuration saved to .env"