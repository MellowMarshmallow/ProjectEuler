# Longest Collatz sequence
# n even -> n/2
# n odd  -> 3n+1
# Find longest chain where n < 1,000,000

def get_length(n: int) -> int:
    length = 1
    while n != 1:
        if n % 2 == 0: # even case
            n /= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def brute_force(n: int) -> int:
    max_k, max_l = 0, 0
    for cur_k in range(1, n, 2):
        cur_l = get_length(cur_k)
        if cur_l > max_l:
            max_l = cur_l
            max_k = cur_k
    return max_k

def memoization(lim: int) -> int:
    largest_n, max_step = 2, 1
    memo = {}

    for n in range(2, lim):
        tmp, step = n, 0

        while tmp != 1:
            if tmp not in memo:
                tmp = tmp / 2 if tmp % 2 == 0 else 3 * tmp + 1
                step += 1
            else:
                step += memo[tmp]
                break

        memo[n] = step

        if max_step < step:
            max_step  = step
            largest_n = n

    return largest_n

print(memoization(1000000)) # Output: 837799
