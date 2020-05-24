# Lattice paths

import math

# Solution: use pascal's triangles
def solution(length: int) -> int:
    # combination: nCk (n choose k)
    # return the middle of the triangle
    return math.comb(2 * length, length)

print(solution(20)) # Output: 137846528820
