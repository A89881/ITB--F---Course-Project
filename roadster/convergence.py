import roadster

# Change working directory to the scripts directory 
# Additional, due to computer errors, recommended by ChatGPT
import os
os.chdir(os.path.dirname(__file__))

n = 1000
list_of_nodes = [n*2**i for i in range(10)]
outputs = []
for n in list_of_nodes:
    T = roadster.time_to_destination(50, 'speed_anna.npz', n)
    outputs.append(T)

T_theoretical =  roadster.time_to_destination(50, 'speed_anna.npz', 100000000) 
errors = [abs(T - T_theoretical) for T in outputs]
print(errors)