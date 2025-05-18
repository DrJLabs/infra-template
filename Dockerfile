FROM python:3.12-slim AS base

WORKDIR /app
COPY requirements-test.txt .
# Dependencies are provided by the runtime environment; no installation step

FROM base AS test
COPY src /app/src
CMD ["pytest", "-q", "src/features"]

