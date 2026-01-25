#!/usr/bin/env python3
import roadster 
import matplotlib.pyplot as plt
import numpy as np

# Creates the scatter plot based on the data from roadster module
# Uses the roadster.load_route function to load the data
source_file = r'speed_anna.npz'
help(roadster.load_route)

distance_km, speed_kmph = roadster.load_route(source_file) # type: ignore
plt.scatter(distance_km, speed_kmph, s=1)
plt.xlabel('Distance (km)')
plt.ylabel('Speed (km/h)')
plt.title('Velocity - Distance from route data')
plt.grid()
plt.show()