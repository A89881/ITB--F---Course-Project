#!/usr/bin/env python3
import roadster 
import matplotlib.pyplot as plt
import numpy as np

# Change working directory to the scripts directory 
# Additional, due to computer errors, recommended by ChatGPT
import os
os.chdir(os.path.dirname(__file__))


# Creates the scatter plot based on the data from roadster module
# Uses the roadster.load_route function to load the data
source_file_1 = "speed_anna.npz"
source_file_2 = "speed_elsa.npz"


# Debugging help commands

# help(roadster.load_route)
# help(roadster.velocity)
# help(roadster.save_route)

# Load raw-data from the source files 
distance_km1, speed_kmph1 = roadster.load_route(source_file_1) # type: ignore
distance_km2, speed_kmph2 = roadster.load_route(source_file_2) # type: ignore

# Load the interpolated data using roadster.velocity function
# Create an array of 1000000000 points between 0 and the last distance of each route
n = 10**3
x1 = np.linspace(0, distance_km1[-1], n)
v1 = roadster.velocity(x1, source_file_1) # type: ignore

x2 = np.linspace(0, distance_km2[-1], n)
v2 = roadster.velocity(x2, source_file_2) # type: ignore

# Plot the raw-data scatter plot
plt.scatter(distance_km1, speed_kmph1, s=1, marker="o" , c="blue", label="Anna - Raw data")
plt.scatter(distance_km2, speed_kmph2, s=1, marker="s" ,c="red", label="Elsa - Raw data")

# Plot the interpolated data line plot
plt.plot(x1, v1, c="green", label="Anna - Interpolated")
plt.plot(x2, v2, c="yellow", label="Elsa - Interpolated")

plt.xlabel("Distance (km)")
plt.ylabel("Speed (km/h)")
plt.legend()
plt.title(f"Velocity - Distance from route data 10e{np.log10(n):.0f} points")
plt.grid()
plt.savefig("interpolation_plot.png") # Save the plot as a PNG file
plt.show()