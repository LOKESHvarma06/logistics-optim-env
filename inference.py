import os
import uvicorn
from fastapi import FastAPI
from openenv_core.api import create_app
from env import LogisticsEnv

# 1. Initialize your custom logistics environment
env = LogisticsEnv()

# 2. Use the Meta OpenEnv 'create_app' helper to turn it into a web API
# This is what the Meta judges' script connects to!
app = create_app(env)

if __name__ == "__main__":
    # Hugging Face and Meta expect port 7860
    uvicorn.run(app, host="0.0.0.0", port=7860)
