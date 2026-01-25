#!/usr/bin/env python3
import numpy as np
import roadster

speed_kmph = np.linspace(1., 200., 1000)
# speed_kmph = np.linspace(1., 10., 10) # Used for testing
consumption_Whpkm = roadster.consumption(speed_kmph) # type: ignore
# print(type(consumption_Whpkm)) # Used for testing
