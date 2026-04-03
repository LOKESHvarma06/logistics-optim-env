import uuid
from openenv.core.env_server import Environment
from models import LogisticsAction, LogisticsObservation, LogisticsState

class LogisticsEnvironment(Environment):
    SUPPORTS_CONCURRENT_SESSIONS = True

    def __init__(self):
        self._state = LogisticsState()
        self._fuel = 100.0
        self._pos = 0

    def reset(self, **kwargs) -> LogisticsObservation:
        self._pos = 0
        self._fuel = 100.0
        self._state = LogisticsState(episode_id=str(uuid.uuid4()), step_count=0)
        return self._get_obs("Vehicle ready at Depot (Node 0).")

    def step(self, action: LogisticsAction) -> LogisticsObservation:
        self._state.step_count += 1
        
        # 1. Physics: Fuel consumption
        cost = 15.0 if action.speed_mode == "POWER" else 8.0
        self._fuel -= cost
        self._pos = action.move_to_node

        # 2. Logic: Win/Loss
        won = (self._pos == self._state.target_node)
        lost = (self._fuel <= 0)
        done = won or lost

        # 3. RL Reward: +1 for winning, -0.01 per step to encourage speed
        reward = 1.0 if won else -0.01
        if lost and not won: reward = -1.0 # Penalty for running out of fuel

        return LogisticsObservation(
            done=done, reward=reward,
            current_node=self._pos,
            fuel_level=self._fuel,
            active_traffic={2: 1.5}, # Node 2 is currently congested
            message="Package Delivered!" if won else "Moving..."
        )

    def _get_obs(self, msg: str) -> LogisticsObservation:
        return LogisticsObservation(
            done=False, reward=0.0, current_node=self._pos,
            fuel_level=self._fuel, active_traffic={}, message=msg
        )

    @property
    def state(self) -> LogisticsState:
        return self._state