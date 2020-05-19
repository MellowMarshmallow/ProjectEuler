def solution():
    # Fill array with Fibonacci sequence terms
    # such that last term is less than 4,000,000
    fib = [1, 2]
    while fib[-1] < 4000000:
        fib.append(fib[-1] + fib[-2])

    # Find the sum of the even-valued terms in the array
    total = 0
    for term in fib:
        if term % 2 == 0:
            total += term

    return total

print(solution()) # Output: 4613732
