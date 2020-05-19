def solution():
    total = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(solution()) # Output: 233168
