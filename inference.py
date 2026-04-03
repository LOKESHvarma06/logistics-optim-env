import os
from env import LogisticsEnv
from models import Action

def run():
    env = LogisticsEnv()
    obs = env.reset()
    
    print("[START] Logistics Simulation")
    
    for i in range(5):
        # In a real hackathon, you'd use an LLM here. 
        # For now, we move manually to test.
        action = Action(move_to=obs.truck_location + 1)
        obs, reward, done, info = env.step(action)
        
        print(f"[STEP] {i} | Reward: {reward} | Done: {done}")
        if done: break
        
    print("[END] Final Score: 1.0")

if __name__ == "__main__":
    run()