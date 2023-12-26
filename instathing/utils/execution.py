# Imports
import random

import time


# Time Sleep function
def time_sleep(
    t:float = 0.0,
    max_var:float = 0.0
) -> float:
    """
    Adds a randomized delay to program execution.

    Parameters:
    - t (float): base delay time (in seconds); 
    - max_var (float): maximum variation as a fraction of t.
        - max_var=1.0 means "100% of t".

    Returns:
    - t_delay (float): calculated delay time.
    """
    # Get random variation within [0, max_var]
    var = round(random.uniform(0, max_var), 4)
    
    # Calculate delay time
    t_delay = t + var*t

    # Sleep for t_delay seconds
    time.sleep(t_delay)

    # Debug
    print(f'Waited for {t_delay:.4f} seconds.')

    # Return t_delay
    return t_delay