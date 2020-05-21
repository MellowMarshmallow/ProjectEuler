# Sum of prime numbers < 2,000,000

def get_primes(n): # Sieve of Eratosthenes
    if n < 2:
        return []

    n += 1
    N = [True] * n
    N[0] = N[1] = False

    i, j = 2, 0

    while i * i < n:
        if N[i]:
            j = i * i
            while j < n:
                N[j] = False
                j += i
        i += 1

    return [prime for prime, key in enumerate(N) if key]

def solution(n):
    return sum(get_primes(n))

print(solution(2000000)) # Output: 142913828922
