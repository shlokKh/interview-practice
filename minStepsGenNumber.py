def minStepsNumber(n):
    min_steps = 0
    curr_val = 1
    while curr_val < n:
        min_steps += 1
        curr_val *= 2
    
    stack = []
    stack.append((curr_val, min_steps))
    while len(stack):
        print(stack)
        val, step = stack.pop()
        if val == n:
            return step
        if val > n:
            stack.append((val*2, step+1))
            if val//3 > 0:
                stack.append((val//3, step+1))
        else:
            if val//3 > 0:
                stack.append((val*2, step+1))
    
    return None


print(minStepsNumber(3))
