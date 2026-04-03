from typing import List, Dict, Optional
from openenv.core.env_server import Action, Observation, State

class LogisticsAction(Action):
    move_to_node: int  # The ID of the next intersection
    speed_mode: str    # "ECO" or "POWER"

class LogisticsObservation(Observation):
    current_node: int
    fuel_level: float
    active_traffic: Dict[int, float] # Node -> Delay factor
    message: str

class LogisticsState(State):
    target_node: int = 4
    fuel_capacity: float = 100.0
    graph: Dict[int, List[int]] = {
        0: [1, 2], 1: [0, 3], 2: [0, 3, 4], 3: [1, 2, 4], 4: [2, 3]
    }