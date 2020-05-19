import math

def get_set_of_primes(n):
    # Sieve of Eratosthenes (algorithm)
    if n < 2:
        return []
    # This function will fail if n is too large since this algorithm is
    # not very space/memory efficient
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False
    i, j = 2, 0
    while i * i < n + 1:
        if numbers[i]:
            j = i * i
            while j < n + 1:
                numbers[j] = False
                j += i
        i += 1
    return [i for i, val in enumerate(numbers) if val]

def solution(n):
    # Only need up to square root of n
    primes, index, largest = get_set_of_primes(int(math.sqrt(n))), 0, 0
    while primes[index] < n:
        # Check that n / primes[index] is a natural number (not float)
        if (n / primes[index]) == int(n / primes[index]):
            n /= primes[index]
            largest = primes[index]
            index = 0
        else:
            index += 1
    # Compare largest factor so far with the remainder
    return max(largest, int(n))

print(solution(600851475143)) # Output: 6857
