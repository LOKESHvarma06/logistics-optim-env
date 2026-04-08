import uvicorn
import sys
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# 1. Handle the library name change with a fallback
try:
    from openenv.core.api import create_app
except (ImportError, ModuleNotFoundError):
    try:
        from openenv_core.api import create_app
    except ImportError:
        print("Error: openenv-core not found. Check Dockerfile installation.")
        sys.exit(1)

from env import LogisticsEnv
from models import Action, Observation

# 2. Define a factory function (Safe for all validator versions)
def env_factory():
    return LogisticsEnv()

# 3. Create the FastAPI app using the factory
app = create_app(
    env_factory, 
    Action, 
    Observation, 
    env_name="logistics-optim"
)

# ROOT ROUTE: Prevents the 404 Health Check error
@app.get("/")
async def root():
    return JSONResponse(content={
        "status": "online",
        "message": "Logistics Optimization Environment is Ready",
        "version": "1.0"
    })

if __name__ == "__main__":
    # Port 7860 is mandatory for Hugging Face Spaces
    uvicorn.run(app, host="0.0.0.0", port=7860)
