'''
[1] : it has to be just the first one

[1, 5] or [5, 1] : it has to either be the first element or the second element

[3, 8, 4], [4, 3, 8], or [8, 4, 3] we start with the first element
check with the 3rd element or 4th element
then we want to check 2nd element with 
'''
from functools import lru_cache

def helper(nums):
    if len(nums) == 0:
        return 0
    return max(nums[0] + helper(nums[2:]), nums[0] + helper(nums[3:]))

def bruteForce(nums):
    return helper(nums)

def dynamicProgramming(nums):
    dp = [0]*(len(nums)+1)
    dp[1] = nums[0]
    for i in range(2, len(nums)+1):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
    return dp[-1]

print(bruteForce([2,7,9,3,1]))
print(dynamicProgramming([2,7,9,3,1]))

'''
If we make a slight modification to this problem and say that the houses are arranged in a circle
Then we have to choose between robbing the first or the last house and take the max of that
'''

def houseRobber2(nums):
    return max(dynamicProgramming(nums[1:]), dynamicProgramming(nums[:-1]))

print(houseRobber2([2,7,9,3,100]))