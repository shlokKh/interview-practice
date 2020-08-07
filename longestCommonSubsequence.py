'''
Brute force approach to this problem
1. Lets assume we are starting from the back
2. We have two cases
    a. Letters are equal from both
    b. Or we have to add 
'''
def bruteForce(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    
    if s1[-1] == s2[-1]:
        return 1 + bruteForce(s1[:-1], s2[:-1])
    
    return max(bruteForce(s1[:-1], s2), bruteForce(s1, s2[:-1]))

def dynamicProgramming(s1, s2):
    dp = [[0]*(len(s2)+1) for i in range(len(s1)+1)]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

def dynamicProgrammingSpaceOpt(s1, s2):
    #TODO this isn't done should be soon tho


    print(dp)


print(bruteForce('AGGTAB', 'GXTXAYB'))
print(dynamicProgramming('AGGTAB', 'GXTXAYB'))
    