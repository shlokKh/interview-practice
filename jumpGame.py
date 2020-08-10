from functools import lru_cache


def bruteForce(nums):
    @lru_cache(maxsize=None)
    def helper(i):
        if i >= len(nums):
            return False
        if i == len(nums)-1:
            return True
        
        curr = 1
        while curr <= nums[i]:
            if helper(curr+i):
                return True
            curr += 1
        return False
    
    return helper(0)



def dynamicProgramming(nums):
    max_ahead = 0
    
    for i in range(len(nums)):
        if i > max_ahead:
            return False
        
        max_ahead = max(max_ahead, i + nums[i])
    
    return True

print(bruteForce([2,0]))

print(dynamicProgramming([2,0]))