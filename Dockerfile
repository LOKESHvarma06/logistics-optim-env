FROM python:3.11-slim

# 1. System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. THE CRITICAL CHANGE: Use standard pip to install globally
# This ensures 'python inference.py' can ALWAYS find the library
RUN pip install --no-cache-dir openenv-core==0.2.0 fastapi uvicorn pydantic

# 3. Copy your project files
COPY . .

# 4. Set Environment Path
ENV PYTHONPATH=/app
EXPOSE 7860

# 5. Run it directly
CMD ["python", "inference.py"]
