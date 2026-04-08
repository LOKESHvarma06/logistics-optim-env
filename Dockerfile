FROM python:3.11-slim

# 1. Essential system tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. THE FIX: Force install globally BEFORE copying anything else
# This ensures a clean install that isn't blocked by local files
RUN pip install --upgrade pip
RUN pip install --no-cache-dir openenv-core==0.2.0 fastapi uvicorn pydantic

# 3. Copy your project files
# Make sure this is on ONE line with a space between the dots
COPY . .

# 4. Set Environment Variables
ENV PYTHONPATH=/app
EXPOSE 7860

# 5. Entry point
CMD ["python", "inference.py"]
