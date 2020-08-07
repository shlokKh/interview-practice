'''
Since we are generating all the possible sub strings of s we are goign to use O(2^n)
'''
def helper(s, wordDict):
    if s  == '':
        return True
    
    for i in range(1, len(s)+1):
        substring = s[:i]
        recursive = s[i:]
        if substring in wordDict and helper(s[i:], wordDict):
            return True
    
    return False


def bruteForce(s, wordDict):
    return helper(s, set(wordDict))

def dynamicProgramming(s, wordDict):
    wordDict = set(wordDict)
    dp = [False]*(len(s)+1)
    dp[0] = True

    for l in range(1, len(s)+1):
        for i in range(l):
            prevWord = dp[i]
            substring = s[i:l]
            if dp[i] and s[i:l] in wordDict:
                dp[l] = True
                break
    
    return dp[-1]

print(bruteForce('applepenapplepens' , ["apple", "pen"]))
print(dynamicProgramming('applepenapplepen' , ["apple", "pen"]))