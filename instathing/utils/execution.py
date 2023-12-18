# Imports
import random

import time


# Time Sleep function
def time_sleep(
    t_base:float = 0.0,
    max_var:float = 0.0
) -> None:
    """
    Add a delay of t_base plus up to 100% of t_base to program execution.

    Parameters:
        t_base (float): base delay time (in seconds); 
        
        max_var (float): maximum variation as a fraction of t_base.
            e.g.: max_var=0.5 means "a maximum variation of 50% of t_base"

    Returns:
        None
    """
    # Get random variation within [0, max_var]
    var = round(random.uniform(0, max_var), 4)
    
    # Calculate t
    t = t_base + var * t_base

    # Sleep for t seconds
    time.sleep(t)

    # Debug
    print(f'Waited for {t:.6f} seconds.')

    # Return None
    return None