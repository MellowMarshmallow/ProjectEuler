def solution():
    # sum and then square
    # sum = N(N+1)/2
    a = (100 * (100 + 1) / 2) ** 2

    # square then sum
    b = 0
    for n in range(1, 101):
        b += n ** 2

    return int(a - b)

print(solution()) # Output: 25164150
