def mm1_queue_measures(arrival_rate, service_rate):
    # Calculate traffic intensity (ρ)
    rho = arrival_rate / service_rate

    # Calculate average number of customers in the system (L)
    L = rho / (1 - rho)

    # Calculate average number of customers in the queue (Lq)
    Lq = rho ** 2 / (1 - rho)

    # Calculate average time a customer spends in the system (W)
    W = 1 / (service_rate - arrival_rate)

    # Calculate average time a customer spends waiting in the queue (Wq)
    Wq = rho / (service_rate - arrival_rate)

    # Calculate probability that the system is empty (P0)
    P0 = 1 - rho

    return L, Lq, W, Wq, P0


# Example usage
arrival_rate = 3  # customers per minute
service_rate = 4  # customers per minute

L, Lq, W, Wq, P0 = mm1_queue_measures(arrival_rate, service_rate)

# Print results
print(f"Average number of customers in the system (L): {L:.2f}")
print(f"Average number of customers in the queue (Lq): {Lq:.2f}")
print(f"Average time a customer spends in the system (W): {W:.2f} minutes")
print(f"Average time a customer spends waiting in the queue (Wq): {Wq:.2f} minutes")
print(f"Probability that the system is empty (P0): {P0:.2f}")
