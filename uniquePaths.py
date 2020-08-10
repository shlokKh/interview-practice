from functools import lru_cache
'''
O(max(2^m, 2^n))
'''
@lru_cache(maxsize=None)
def helper(m, n):
    if m < 1 or n < 1:
        return 0
    if m == 1 and n == 1:
        return 1
    return helper(m-1, n) + helper(m, n-1)

def bruteForce(m: int, n: int) -> int:
    return helper(m, n)

def dynamicProgramming(m, n):
    dp = [[0]*(m) for i in range(n)]

    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]

    return dp[n-1][m-1]

def dyanmicProgrammingSpace(m, n):
    curr = [1]*m

    for i in range(1, n):
        for j in range(1, m):
            curr[j] += curr[j-1]
        

    return curr[-1]

p1, p2 = 4, 4
print(dynamicProgramming(4, 4))
print(dyanmicProgrammingSpace(4, 4))