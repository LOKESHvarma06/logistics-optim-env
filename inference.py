import uvicorn
import sys
from fastapi import FastAPI

# 1. Clean Import Logic
try:
    # Try the most recent name first
    from openenv.core.api import create_app
except (ImportError, ModuleNotFoundError):
    try:
        # Fallback to the legacy name
        from openenv_core.api import create_app
    except ImportError:
        print("CRITICAL: openenv-core not found in python path.")
        sys.exit(1)

from env import LogisticsEnv
from models import Action, Observation

# 2. Use a factory to avoid state issues during validation
def env_factory():
    return LogisticsEnv()

app = create_app(env_factory, Action, Observation)

@app.get("/")
async def health_check():
    return {"status": "ready"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
