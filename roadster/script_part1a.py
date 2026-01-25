#!/usr/bin/env python3
import numpy as np
import roadster

speed_kmph = np.linspace(1., 200., 1000)
consumption_Whpkm = roadster.consumption(speed_kmph)
