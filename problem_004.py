def check_if_palindrome(n):
    # Convert n to string, then map to apply int on it
    # Then return a list
    arr = list(map(int, str(n)))
    while len(arr) != 0 and len(arr) != 1:
        if (arr[0] != arr[-1]):
            return False
        # Remove first and last element
        arr.pop(0)
        arr.pop(-1)
    return True

def solution():
    largest = 0
    # Check the lower triangle of the "matrix"
    # |\
    # |_\
    for i in range(100,1000):
        for j in range(i, 1000):
            if check_if_palindrome(i * j) and largest < i * j:
                largest = i * j
    return largest

print(solution()) # Output: 906609
