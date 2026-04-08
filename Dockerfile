FROM python:3.11-slim

# 1. Install essential build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. FORCE INSTALL: This is the most important line
RUN pip install --no-cache-dir openenv-core==0.2.0 fastapi uvicorn pydantic

# 3. Copy project files
COPY . .

# 4. Set Environment Variables
ENV PYTHONPATH=/app
EXPOSE 7860

# 5. Entry point
CMD ["python", "inference.py"]
