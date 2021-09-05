import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Env-v0',
    entry_point='Gym_env.envs:twoarmedbandit',
    timestep_limit=1,
    reward_threshold=1.0,
    nondeterministic = True,
)
