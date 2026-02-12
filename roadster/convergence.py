import roadster
import numpy as np
import matplotlib.pyplot as plt

# Change working directory to the scripts directory 
# Additional, due to computer errors, recommended by ChatGPT
import os
os.chdir(os.path.dirname(__file__))

# Define source file
source_file1 = "speed_anna.npz"
source_file2 = "speed_elsa.npz"

# Define list of nodes for convergence study
n = 10**3 # Arbitrary initial number of nodes
list_of_nodes = [n*2**i for i in range(10)]

# General max distance data definition
distance_km1, speed_kmph1 = roadster.load_route(source_file1) # type: ignore
distance_km2, speed_kmph2 = roadster.load_route(source_file2) # type: ignore

# Convergence study - Output list
outputs = []

print(list_of_nodes)
# Convergence loop to calculate time to destination for different number of nodes
for n in list_of_nodes:
    T = roadster.time_to_destination(distance_km1[-1], 'speed_anna.npz', n) # type: ignore
    outputs.append(T)

# Theoretical value for error calculation, using a very large number of nodes as reference (Anna's route)
T_theoretical =  roadster.time_to_destination(distance_km1[-1], 'speed_anna.npz', 10**7)  # type: ignore
E_theoretical = roadster.total_consumption(distance_km1[-1], 'speed_anna.npz', 10**7) # type: ignore
print(f"Theoretical Time to Destination: {T_theoretical} hours")
print(f"Theoretical Total Energy Consumption: {E_theoretical} Wh")

# Theoretical value for error calculation, using a very large number of nodes as reference (Elsa's route)
T_theoretical_elsa =  roadster.time_to_destination(distance_km2[-1], 'speed_elsa.npz', 10**7)  # type: ignore
E_theoretical_elsa = roadster.total_consumption(distance_km2[-1], 'speed_elsa.npz', 10**7) # type: ignore
print(f"Theoretical Time to Destination: {T_theoretical_elsa} hours")
print(f"Theoretical Total Energy Consumption: {E_theoretical_elsa} Wh")

# Calculate and print errors
errors = [abs(T - T_theoretical) for T in outputs]
errors_float = [float(i) for i in errors]
print(errors_float)

# Plotting convergence results

# Plotting the convergence results on a log-log scale
plt.plot(list_of_nodes, errors_float, marker='o')
plt.xscale('log') 
plt.yscale('log')
# Adding a reference line for O(n^-2) convergence
plt.plot(list_of_nodes, [errors_float[0]*(n/list_of_nodes[0])**(-2) for n in list_of_nodes], label='O(n^-2)', linestyle='--')
plt.xlabel('Number of Nodes (log scale)')   
plt.ylabel('Absolute Error (log scale)')
plt.title('Convergence of Time to Destination with Increasing Nodes')   
plt.grid()
plt.savefig("convergence_plot.png") # Save the plot as a PNG file
plt.show()      