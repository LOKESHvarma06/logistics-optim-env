import uvicorn
from openenv.core.env_server import create_fastapi_app
from server.environment import LogisticsEnvironment
from models import LogisticsAction, LogisticsObservation

# The function needs to know the Logic Class, the Action Class, and the Observation Class
app = create_fastapi_app(
    LogisticsEnvironment, 
    action_cls=LogisticsAction, 
    observation_cls=LogisticsObservation
)

def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()