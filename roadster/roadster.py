import numpy as np
from scipy import interpolate

# Change working directory to the scripts directory 
# Additional, due to computer errors, recommended by ChatGPT
import os
os.chdir(os.path.dirname(__file__))

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    # Consumption polynomial coefficients
    a1, a2, a3, a4 = 546.8, 50.31, 0.2584, 0.00821
    
    # Define consumption as a function of speed
    poly = lambda v: a1*v**(-1) + a2 + a3*v + a4*v**2
    
    # Return consumption value(s)
    if np.all(v >= 0):
        return poly(v)
    else:
        raise ValueError("Speed must be non-negative")
    
### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

### PART 2A ###
def time_to_destination(x: float, route, n):
    # Determine step size, based on n intervals
    h = (x - 0) / (n)
    
    # Create array of x values (and n+1 points)
    x_values = np.linspace(0, x, n + 1) 
    
    # Define function to integrate
    f = lambda x: 1 / velocity(x, route) # type: ignore
    
    # Apply trapezoidal rule
    I_trap = (h/2)*(f(x_values[0]) + 2 * sum(f(x_values[1:n])) + f(x_values[-1]))
    
    # Return result
    return I_trap

### PART 2B ###
def total_consumption(x, route, n):
    # Determine step size, based on n intervals
    h = (x - 0) / n
    # Create array of x values (and n+1 points)
    x_values = np.linspace(0, x, n + 1)
    # Define function to integrate
    f = lambda x: consumption(velocity(x, route)) # type: ignore
    # Apply trapezoidal rule
    I_trap = (h/2)*(f(x_values[0]) + 2 * sum(f(x_values[1:n])) + f(x_values[-1]))
    # Return result
    return I_trap

### PART 3A ###
def distance(T, route): 
    # Tolerance for convergence
    tol = 10**(-4)
    
    # Function to find root of f(x) = time_to_destination(x, route) - T => time_to_destination(x, route) = T
    """
    Relevant Comment: use large n for better accuracy, 
    otherwise Newton's method may not converge well
    """
    f = lambda x: time_to_destination(x, route, 10**6) - T 
    
    # Derivative f'(x) = 1 / velocity(x, route) <== Fundamental Theorem of Calculus
    df = lambda x: 1 / velocity(x, route)  # type: ignore
    
    
    # Newton's method implementation
    # Initial guess, using velocity at 0 km
    # From T = x / v  =>  x = v * T
    x0 = velocity(0, route) * T  # type: ignore 
    
    # Arbitrary large number of max iterations
    max_iter = 10**3
    
    # Iteration loop; stop if within tolerance or max iterations reached
    for i in range(max_iter):
        # Perform Newton's method step
        x1 = x0 - f(x0) / df(x0)
        
        # Check for convergence
        if abs(x1 - x0) <= tol:
            return x1
        
        # Update x0 for next iteration
        x0 = x1

### PART 3B ###
def reach(C, route):
    # Tolerance for convergence
    tol = 10**(-4)

    # Function to find root of f(x) = total_consumption(x, route) - C => total_consumption(x, route) = C
    """
    Relevant Comment: use large n for better accuracy, 
    otherwise Newton's method may not converge well
    """
    f = lambda x: total_consumption(x, route, 10**6) - C
    
    # Derivative f'(x) = consumption(velocity(x, route))
    df = lambda x: consumption(velocity(x, route))  # type: ignore
    
    # Newton's method implementation
    # Initial guess, using initial consumption value at 0 km
    # From C = consumption(v) * x  =>  x = C / consumption(v)
    x0 = C / consumption(velocity(0, route))  # type: ignore
    
    # System boundaries
    max_distance = max(load_route(route)[0])
    min_distance = min(load_route(route)[0])
    
    # Arbitrary large number of max iterations
    max_iter = 10**3
    # Iteration loop; stop if within tolerance or max iterations reached
    for i in range(max_iter):
        
        # Ensure x0 stays within valid distance range
        if min_distance < x0 < max_distance:
            
            # Perform Newton's method step
            x1 = x0 - f(x0) / df(x0)
            
            # Check for convergence
            if abs(x1 - x0) <= tol:
                return x1
            
            # Update x0 for next iteration
            x0 = x1
        else:
            if x0 >= max_distance:
                return max_distance
            return min_distance