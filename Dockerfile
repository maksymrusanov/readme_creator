FROM astral/uv:0.11.15-python3.13-alpine AS builder

RUN apk add --no-cache uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project
COPY . .
RUN uv sync --frozen --no-editable
FROM astral/uv:0.11.15-python3.13-alpine
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
CMD ["uv", "run", "python3", "main.py"]
