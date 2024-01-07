# Imports
from random import uniform
from time import sleep


def time_sleep_var(
    t:float = 0.000,
    delay:float = 000.00
) -> float:
    """
    Adds a randomly-delayed time.sleep() call to program execution
    
    Calls time.sleep(x), where x is a random value in the range [t, t+t_delay]
    
    :param t: Base time (in seconds)
    :type t: float
    :param delay: Delay (0-100% of t)
    :type delay: float
    :return x: Calculated time
    :rtype: float
    """
    # Do not allow negative delay
    if delay<0: 
        delay = 0
    # Do not allow delay over 100%
    elif delay>100:
        delay = 100

    # Calculate delay in seconds
    t_delay = t * (delay / 100)

    # Calculate x
    x = t + (t_delay * round(uniform(0, 1), 3))

    # Call time.sleep(x)
    sleep(x)

    # Return x
    return x