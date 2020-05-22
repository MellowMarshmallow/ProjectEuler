# Triangle numbers

def num_factor(k: int) -> int:
    if k < 1:
        return 0
    if k == 1:
        return 1
    n = 1
    count = 0
    while n * n < k + 1:
        if k % n == 0:
            count += 2
        n += 1
    return count

def solution(n: int) -> int:
    # For natural numbers (expect 1), they all have pairs of divisors
    # So for some n-number k, we only have to check up to sqrt(k)

    # The relationship of a triangle number can be defined as:
    # K_n = K_n-1 + current term number, K_1 = 1

    # We can define a function that returns the number of factors

    # While the function returns false, we can update "K"
    # Then once the function returns true, we return "K"

    # Although I'm not sure, I believe that:
    # number of factors of K_n >= number of factors of K_n-1

    k, term_number = 1, 1

    while num_factor(k) < n:
        term_number += 1
        k += term_number

    return k

print(solution(500)) # Output: 76576500
