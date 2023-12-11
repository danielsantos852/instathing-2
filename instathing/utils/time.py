# Imports
import random
import time


# Wait function
def time_sleep(t_base:float, dt=-1.0) -> None:
    
    # If no dt provided (dt=-1.0): 
    if dt==(-1.0):

        # dt = 15% of t_base
        dt = 0.15*t_base

    # Get random float within [0, 1]
    x = round(random.uniform(0, 1), 6)

    # Calculate t
    t = t_base + (x * dt)

    # Sleep for t seconds
    time.sleep(t)

    # Debug
    print(f'Waited for {t:.6f} seconds.')

    # Return None
    return None