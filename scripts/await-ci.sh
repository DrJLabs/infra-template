#!/bin/sh
# Simple script to await services in CI environment
# Doesn't depend on bash being available (uses POSIX sh instead)

set -e

SERVICE_NAME=$1
HOST=$2
PORT=$3
TIMEOUT=${4:-30}

if [ -z "$SERVICE_NAME" ] || [ -z "$HOST" ] || [ -z "$PORT" ]; then
  echo "Usage: $0 <service_name> <host> <port> [timeout_seconds]"
  echo "Example: $0 postgres postgres 5432 60"
  exit 1
fi

echo "Waiting for $SERVICE_NAME at $HOST:$PORT (timeout: ${TIMEOUT}s)..."
elapsed=0

while ! nc -z "$HOST" "$PORT" >/dev/null 2>&1; do
  if [ $elapsed -ge "$TIMEOUT" ]; then
    echo "Timeout reached waiting for $SERVICE_NAME!"
    exit 1
  fi
  
  echo "Waiting for $SERVICE_NAME... ($elapsed/${TIMEOUT}s)"
  sleep 2
  elapsed=$((elapsed + 2))
done

echo "$SERVICE_NAME is available at $HOST:$PORT!"
exit 0 