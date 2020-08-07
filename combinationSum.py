def helper(nums, target, curr):
    if curr > target:
        return 0
    elif curr == target:
        return 1
    total = 0
    for n in nums:
        total += helper(nums, target, curr+n)
    
    return total
'''
Time Complexity: let len(nums) = m and let target = 
'''
def bruteForce(nums, target):
    return helper(nums, target, 0)

def dynamicProgramming(nums, target):
    dp = [0]*(target+1)
    for n in nums:
        dp[n] = 1
    for i in range(target+1):
        for n in nums:
            if i-n > 0:
                dp[i] += dp[i-n]
    
    return dp[-1]

print(bruteForce([1,2,3], 3))
print(dynamicProgramming([1,2,3], 4))
