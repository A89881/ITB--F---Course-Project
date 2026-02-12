#!/usr/bin/env python3
import numpy as np
import roadster
import matplotlib.pyplot as plt

speed_kmph = np.linspace(1., 200., 1000)
# speed_kmph = np.linspace(1., 10., 10) # Used for testing
consumption_Whpkm = roadster.consumption(speed_kmph) # type: ignore

# Plot the energy consumption vs speed
plt.plot(speed_kmph, consumption_Whpkm)
plt.xlabel("Speed (km/h)")
plt.ylabel("Energy Consumption (Wh/km)")
plt.title("Energy Consumption vs Speed")
plt.grid()
plt.savefig("consumption_plot.png") # Save the plot as a PNG file
plt.show()  

# print(type(consumption_Whpkm)) # Used for testing
