# Imports
from random import uniform
from time import sleep


def time_sleep_randomized(
    t_min:float = 0.0,
    t_max:float = 0.0
) -> float:
    """
    Adds a randomized delay to programm execution

    Calls time.sleep(t), where t is a random value in the range [t_min, t_max]
    
    :param t_min: Minimum delay time (in seconds)
    :type t_min: float
    :param t_max: Maximum delay time (in seconds)
    :type t_max: float

    :return: Drawn number
    :rtype: float
    """
    # Do not allow negative times
    if t_min < 0.0:
        t_min = 0.0
    if t_max < 0.0:
        t_max = 0.0

    # Calculate t
    t = round(uniform(t_min, t_max), 4)

    # Call time.sleep(t)
    sleep(t)

    # Return t
    return t
