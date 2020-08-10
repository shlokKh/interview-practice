def firstDuplicate(a):
    for i in a:
        a[abs(i)-1] *= -1
        if a[abs(i)-1] > 0:
            return abs(i)
    return -1

print(firstDuplicate([2, 1, 4, 3, 5, 3, 2]))