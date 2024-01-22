import numpy as np

def get_actual_hour(hour_sin, hour_cos):
    angle = np.arctan2(hour_sin, hour_cos)
    hour = 24 * angle / (2 * np.pi)

    if hour < 0:
        hour += 24

    return int(hour)

import numpy as np

def calculate_hour_sin_cos(hour):
    hour_sin = np.sin(2 * np.pi * hour / 24)
    hour_cos = np.cos(2 * np.pi * hour / 24)
    
    return (hour_sin, hour_cos)
