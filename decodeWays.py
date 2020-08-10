'''
'' -> 0 ways
'1' -> if there is one digit there is only 1 way
'12' -> if there are two digits there r 2 ways
'226' -> if there are three digits there r 3 ways

check if the two le
'''
from functools import lru_cache
'''
O(2^n) not really anymore because we cache, but w/o caching
'''

@lru_cache(maxsize=None)
def helper(s):
    if len(s) == 0:
        return 1
    if len(s) == 2 and s[0] == '0':
        return 0
    total = 0

    if len(s) >= 2 and int(s[:2]) <= 26:
        total += helper(s[2:])
    
    total += helper(s[1:])
    return total

def bruteForce(s):
    return helper(s)

'''
O(n) lets gooooooooo :) 
'''
def dynamicProgramming(s):
    dp = [0]*(len(s)+1)
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, len(s)+1):
        first = int(s[i-1:i])
        second = int(s[i-2:i])
        if first >= 1 and first <= 9:
            dp[i] += dp[i-1]
        if second >= 10 and second <= 26:
            dp[i] += dp[i-2]

    return dp[-1]

print(bruteForce("226"))
print(dynamicProgramming("12"))