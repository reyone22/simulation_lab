import random
import math

def function(x):
    # Define the function for which you want to estimate the area under the curve
    return x**2  # Example: y = x^2

def monte_carlo_area(num_points, x_min, x_max, y_min, y_max):
    area = 0
    for _ in range(num_points):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        if y <= function(x):
            area += 1
    
    area_estimate = (y_max - y_min) * (x_max - x_min) * area / num_points
    return area_estimate

# Define the interval and range for the curve
x_min = 0
x_max = 2
y_min = 0
y_max = 4

# Set the desired number of points
num_points = 100

# Estimate the area under the curve
estimated_area = monte_carlo_area(num_points, x_min, x_max, y_min, y_max)
print(f"Estimated area under the curve : {estimated_area:.6f}")

# Calculate the exact area under the curve (for comparison)
exact_area = 4.0 / 3.0  # For the example function y = x^2 from 0 to 2
