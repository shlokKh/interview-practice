from collections import defaultdict
from typing import List

def longestConsecutive(nums: List[int]) -> int:
    graph = {}
    for n in nums:
        if n not in graph:
            graph[n] = set()

        if n-1 in graph:
            graph[n-1].add(n)
            graph[n].add(n-1)
        if n+1 in graph:
            graph[n+1].add(n)
            graph[n].add(n+1)
    
    visited = set()
    def dfs(node, consecutive):
        visited.add(node)
        consecutive += 1
        for edge in graph[node]:
            if edge not in visited:
               consecutive = max(dfs(edge, consecutive), consecutive)

        return consecutive

    maxConsecutive = 0
    for node in graph:    
        if node not in visited:
            consecutive = dfs(node, 0)
        maxConsecutive = max(maxConsecutive, consecutive)
    
    return maxConsecutive


def longestConsecutiveEasy(nums):
    nums = set(nums)
    best = 0
    iterations = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
                iterations += 1
            best = max(best, y - x)
        iterations += 1
    print(iterations)
    return best


print(longestConsecutiveEasy([1,2,3,4,5,6,7, 8, 9, 10,]))