import random
from models import Observation, Action

class LogisticsEnv:
    def __init__(self):
        self.location = 0
        self.destination = 5
        self.fuel = 100.0

    def reset(self):
        self.location = 0
        self.fuel = 100.0
        return self.get_obs()

    def step(self, action: Action):
        # Move the truck
        self.location = action.move_to
        self.fuel -= 10.0  # Lose fuel every move
        
        # Calculate Reward
        reward = 0.0
        done = False
        
        if self.location == self.destination:
            reward = 1.0  # Big win!
            done = True
        elif self.fuel <= 0:
            reward = -1.0 # Out of fuel!
            done = True
        else:
            reward = 0.1  # Small point for moving
            
        return self.get_obs(), reward, done, {}

    def get_obs(self):
        # In a simple 0-1-2-3-4-5 line, possible moves are neighbors
        moves = [self.location + 1] if self.location < 5 else []
        return Observation(
            truck_location=self.location,
            destination=self.destination,
            fuel_left=self.fuel,
            possible_moves=moves
        )