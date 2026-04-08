FROM python:3.11-slim

# 1. Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 2. Install 'uv'
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY . .

# 3. CRITICAL: Install dependencies globally so the validator's 
# 'python inference.py' command can see them!
RUN uv pip install --system --no-cache openenv-core==0.2.0 fastapi uvicorn pydantic

# 4. Set Environment Path
ENV PYTHONPATH=/app

EXPOSE 7860

# 5. Updated CMD to run inference.py as the entry point
CMD ["python", "inference.py"]
