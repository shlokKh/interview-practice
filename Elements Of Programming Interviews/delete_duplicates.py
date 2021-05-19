'''
a is a sorted array that we want to remove all the duplicate elements for:
[2,3,5,5,7,11,11,11,13] -> [2,3,5,7,11,13,0,0,0]
'''
def delete_duplicates(a):
    if not a:
        return None
    idx = 1
    for i in range(1, len(a)):
        if a[idx-1] != a[i]:
            a[idx] = a[i]
            idx += 1

    return a
print(delete_duplicates([2,3,5,5,7,11,11,11,13]))
