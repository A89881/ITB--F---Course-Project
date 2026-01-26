import roadster

# Change working directory to the scripts directory 
# Additional, due to computer errors, recommended by ChatGPT
import os
os.chdir(os.path.dirname(__file__))

# Define source file
source_file = "speed_anna.npz"

# Define list of nodes for convergence study
n = 10**3 # Arbitrary initial number of nodes
list_of_nodes = [n*2**i for i in range(10)]

# General max distance data definition
distance_km, speed_kmph2 = roadster.load_route(source_file) # type: ignore

# Convergence study - Output list
outputs = []

# Convergence loop to calculate time to destination for different number of nodes
for n in list_of_nodes:
    T = roadster.time_to_destination(distance_km[-1], 'speed_anna.npz', n) # type: ignore
    outputs.append(T)

# Theoretical value for error calculation, using a very large number of nodes as reference
T_theoretical =  roadster.time_to_destination(distance_km[-1], 'speed_anna.npz', 100000000)  # type: ignore

# Calculate and print errors
errors = [abs(T - T_theoretical) for T in outputs]
print(errors)