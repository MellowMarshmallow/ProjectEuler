# a^2 + b^2 = c^2
# Find the unique solution to: a + b + c = 1000

# Combine equations: 500 = a + b - ab / 1000

import math

def brute_force():
    # Check lower triangle of a "diagonal matrix"
    for i in range(1, 1000):
        for j in range(i, 1000):
            if i + j - i * j / 1000 == 500:
                return int(i * j * math.sqrt(i ** 2 + j ** 2))

print(brute_force()) # Output: 31875000
