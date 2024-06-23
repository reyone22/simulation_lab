
def multiplicative_congruential_method(X0, a, m, n):
    random_numbers = []
    Xn = X0
    for _ in range(n):
        Xn = (a * Xn) % m
        random_numbers.append(Xn)
    return random_numbers

# Parameters
X0 = 13
m = 1000
a = 15
n = 50

# Generate 50 random numbers
random_numbers = multiplicative_congruential_method(X0, a, m, n)

# Print random numbers with a new line after every 10 numbers
print("Random numbers:")
for i in range(len(random_numbers)):
    print(random_numbers[i], end=' ')
    if (i + 1) % 10 == 0:
        print()