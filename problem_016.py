# Power digit sum

def brute_force(power: int) -> int:
    n, Sum = 2 ** power, 0
    while n:
        Sum, n = Sum + n % 10, n // 10
    return Sum

print(brute_force(1000)) # Output: 1366
