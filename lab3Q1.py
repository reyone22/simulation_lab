import random
import math

def monte_carlo_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1
    
    pi_estimate = 4 * inside_circle / num_points
    return pi_estimate

# Test the function with different numbers of points

print("Estimated value of π with 100,000 points:", monte_carlo_pi(100_000))


# Compare the estimated value with the built-in math.pi value
print("Value of π from math.pi:", math.pi)