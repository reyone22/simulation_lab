# Define the parameters
mean_inter_arrival_time = 10  # in minutes
mean_service_time = 5  # in minutes

# Arrival rate (lambda) and Service rate (mu)
lambda_rate = 1 / mean_inter_arrival_time
mu_rate = 1 / mean_service_time

# Utilization factor (rho)
rho = lambda_rate / mu_rate

# Probability that a customer will not have to wait
P0 = 1 - rho

# Expected number of customers in the system
L = rho / (1 - rho)

# Expected time a customer spends in the system
W = 1 / (mu_rate - lambda_rate)

# Output the results
print(f"a. Probability that a customer will not have to wait at the counter: {P0:.4f}")
print(f"b. Expected number of customers in the bank: {L:.4f}")
print(f"c. Time a customer expects to spend in the bank: {W:.4f} minutes")
