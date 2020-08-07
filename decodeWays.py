'''
'' -> 0 ways
'1' -> if there is one digit there is only 1 way
'12' -> if there are two digits there r 2 ways
'226' -> if there are three digits there r 3 ways

check if the two le
'''
from functools import lru_cache

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

def dynamicProgramming(s):
    dp = [0]*(len(s)+1)

print(bruteForce("226"))