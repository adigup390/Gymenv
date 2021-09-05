import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Env-v0',
    entry_point='Gymenv.envs:Env1',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)
