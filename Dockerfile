# Use a slim Python image for faster downloads
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install 'uv' - the high-speed package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory inside the container
WORKDIR /app

# Copy all project files (honoring your .dockerignore)
COPY . .

# Install dependencies using the uv.lock for 100% stability
RUN uv sync --frozen --no-cache

# Set the Environment Path so Python finds 'models.py' and 'server/'
ENV PYTHONPATH=.

# Hugging Face Spaces strictly requires port 7860
EXPOSE 7860

# Start the server using the absolute path to uvicorn
CMD ["python", "-m", "uv", "run", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]