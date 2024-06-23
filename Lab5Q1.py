import numpy as np


def probability_not_rain_day_after_tomorrow():
    # State transition matrix
    transition_matrix = np.array([
        [0.4, 0.6],  # From Rainy to [Rainy, Not Rainy]
        [0.2, 0.8]  # From Not Rainy to [Rainy, Not Rainy]
    ])

    # Initial state vector for "Not Rainy today"
    initial_state = np.array([0, 1])  # [P(Rainy today), P(Not Rainy today)]

    # Calculate state probabilities after 2 days
    state_after_two_days = initial_state @ np.linalg.matrix_power(transition_matrix, 2)

    # Probability of "Not Rainy" after two days
    probability_not_rain = state_after_two_days[1]

    return probability_not_rain


# Usage
probability = probability_not_rain_day_after_tomorrow()
print(f"The probability of not raining the day after tomorrow, given it's not raining today, is {probability:.2f}")
