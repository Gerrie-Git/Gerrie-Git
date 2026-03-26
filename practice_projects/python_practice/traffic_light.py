#1. Traffic Light Simulator

from enum import Enum
import time


class traffic_light(Enum):
    red = 1
    orange = 2
    green = 3

def traffic_light_sim(timer=2):
    for light in traffic_light:
        print(light.name)
        time.sleep(timer)

if __name__ == "__main__":
    traffic_light_sim()