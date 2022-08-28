from gym.envs.registration import register

register(
    id="LunarLanderVar-v2",
    entry_point="gym_mod.envs:LunarLanderVar",
    max_episode_steps=1000,
    reward_threshold=200,
)

register(
    id="LunarLanderContinuousVar-v2",
    entry_point="gym_mod.envs:LunarLanderContinuousVar",
    max_episode_steps=1000,
    reward_threshold=200,
)