Modified OpenAI Gym environments.
Original source code from https://github.com/openai/gym/

# Environments
1. LunarLanderVar-v2
    LunarLander-v2 modified to have random initial x state.
2. LunarLanderContinuousVar-v2
    LunarLanderContinuous-2 modified to have random initial x state. 

# Installation
pip install -e .

# Usage
import gym_mod
env = gym.make("LunarLanderVar-v2")