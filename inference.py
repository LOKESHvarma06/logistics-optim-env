import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# 1. Handle the library name change
try:
    from openenv.core.api import create_app
except (ImportError, ModuleNotFoundError):
    from openenv_core.api import create_app

from env import LogisticsEnv
from models import Action, Observation

# 2. Create the environment
env = LogisticsEnv()

# 3. Create the FastAPI app
app = create_app(
    env, 
    Action, 
    Observation, 
    env_name="logistics-optim"
)

# 🌟 THE FIX: Add a root route so the validator doesn't get a 404
@app.get("/")
async def root():
    return JSONResponse(content={
        "status": "online",
        "message": "Logistics Optimization Environment is Ready",
        "version": "1.0"
    })

if __name__ == "__main__":
    # Ensure port 7860 is used for Hugging Face
    uvicorn.run(app, host="0.0.0.0", port=7860)
