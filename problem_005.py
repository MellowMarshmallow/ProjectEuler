def get_set_of_primes(n): # Sieve of Erathosetenes
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
    primes = get_set_of_primes(n)
    lcm = 1
    for prime in primes:
        exponent = 1
        while prime ** (exponent + 1) < n:
            exponent += 1
        lcm *= prime ** exponent
    return lcm

print(solution(20)) # Output: 232792560
