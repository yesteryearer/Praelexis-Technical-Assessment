import numpy as np

def fractional_hour(hour, minute, second):
    return hour + (minute / 60) + (second / 3600)

def get_actual_hour(hour_sin, hour_cos):
    angle = np.arctan2(hour_sin, hour_cos)
    if angle < 0:
        angle += 2 * np.pi

    hour = 24 * angle / (2 * np.pi)
    return round(hour) if round(hour) != 24 else 0

def get_fractional_hour(hour_sin, hour_cos):
    angle = np.arctan2(hour_sin, hour_cos)
    if angle < 0:
        angle += 2 * np.pi

    fractional_hour = 24 * angle / (2 * np.pi)
    return fractional_hour if fractional_hour != 24 else 0

def fractional_hour_to_hms(fractional_hour):
    hours = int(fractional_hour)
    minutes_fraction = (fractional_hour - hours) * 60
    minutes = int(minutes_fraction)
    seconds = int((minutes_fraction - minutes) * 60)

    return (hours, minutes, seconds)

def calculate_hour_sin_cos(hour):
    hour_sin = np.sin(2 * np.pi * hour / 24)
    hour_cos = np.cos(2 * np.pi * hour / 24)
    
    return (hour_sin, hour_cos)