def paths_sum(t, sum):
    if t is None:
        return 0

    if t.data > sum:
        return 0
    
    if t.data == sum:
        return 1
    
    return paths_sum(t.left, sum-t.data) + paths_sum(t.right, sum-t.data)
