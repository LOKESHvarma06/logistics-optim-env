import uvicorn
import sys
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# 1. Flexible Import Logic
try:
    from openenv.core.api import create_app
except (ImportError, ModuleNotFoundError):
    try:
        from openenv_core.api import create_app
    except ImportError:
        print("CRITICAL: openenv-core not found in python path.")
        sys.exit(1)

from env import LogisticsEnv
from models import Action, Observation

# 2. Define a factory function to create the environment
def env_factory():
    return LogisticsEnv()

# 3. Create the FastAPI app
app = create_app(
    env_factory, 
    Action, 
    Observation, 
    env_name="logistics-optim"
)

# 4. Root Health Check to prevent 404 errors
@app.get("/")
async def root():
    return JSONResponse(content={
        "status": "online",
        "message": "Logistics Environment Ready",
        "version": "1.0"
    })

if __name__ == "__main__":
    # Must use port 7860 for Hugging Face compatibility
    uvicorn.run(app, host="0.0.0.0", port=7860)
