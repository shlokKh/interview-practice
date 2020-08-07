def check_permutation(s1, s2):
    letters = defaultdict(int)
    for c in s1:
        letters[c] += 1
    
    for c in s2:
        letters[c] -= 1
    
    for k,v in letters.items():
        if v != 0:
            return False
    
    return True

'''
O(n) complexity
O(n) space

'''