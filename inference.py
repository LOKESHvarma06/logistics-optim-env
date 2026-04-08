import uvicorn
from fastapi import FastAPI

# 1. Universal Import: Fixes the ModuleNotFoundError
try:
    from openenv.core.api import create_app
except (ImportError, ModuleNotFoundError):
    from openenv_core.api import create_app

from env import LogisticsEnv
from models import Action, Observation

# 2. Define the environment
env = LogisticsEnv()

# 3. Use the create_app factory
# Note: Newer versions often require Action and Observation models as arguments
app = create_app(
    env, 
    Action, 
    Observation, 
    env_name="logistics-optim"
)

if __name__ == "__main__":
    # Hugging Face and Meta expect port 7860
    uvicorn.run(app, host="0.0.0.0", port=7860)
