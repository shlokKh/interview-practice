def lengthOfLIS(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

def lengthOfLDS(nums):
    tails = []
    sequences = []
    size = 0
    for n in nums:
        i, j = 0, len(tails)
        while i != j:
            m = (i+j) // 2
            if tails[m] < n:
                i = m + 1
            else:
                j = m
        
        if i == len(tails):
            tails.append(n)
            sequences.append([])
        else:
            sequences[i].append(tails[i])
            tails[i] = n
            size = max(size, len(sequences[i])+1)
        
    return size


print(lengthOfLDS([10,5,8,3,9,4,12,11]))
