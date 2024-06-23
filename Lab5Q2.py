import numpy as np

# Transition matrix
P = np.array([
    [0.9, 0.1],  # From Coke
    [0.2, 0.8]   # From Pepsi
])

# Initial state (Pepsi)
initial_state = np.array([0, 1])  # [Coke, Pepsi]

# Calculate the state after two transitions
state_after_two_steps = initial_state @ np.linalg.matrix_power(P, 2)

# Probability of purchasing Coke after two steps
prob_coke = state_after_two_steps[0]

print("Probability of purchasing Coke after two purchases starting from Pepsi:", prob_coke)
