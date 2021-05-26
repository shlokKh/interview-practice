import math

def real_sqr(x):
    low, high = (x, 1) if x < 1 else (1, x)

    while not math.isclose(low, high):
        mid = (low + high) * .5
        mid_squared = mid*mid
        if mid_squared > x:
            high = mid
        else:
            low = mid
    
    return low

print(real_sqr(4))
