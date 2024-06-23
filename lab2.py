import math

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Function to calculate Poisson distribution
def poisson_distribution(x, lambda_value):
    return (math.exp(-lambda_value) * (lambda_value ** x)) / factorial(x)

# Average rate of occurrence (cars/hr)
lambda_value = 12

# Generate Poisson distribution for x = 0, 1, 2, ..., 15
for x in range(16):
    probability = poisson_distribution(x, lambda_value)
    print(f"P(X={x}) = {probability:.6f}")