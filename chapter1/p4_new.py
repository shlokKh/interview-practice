def palindrom_permutation(s):
    letters = defaultdict(int)
    str_len = 0
    for c in s:
        letters[c] += 1
        str_len += 1

    num_odd = 0
    for k,v in letters.items():
        if len % 2 == 0 and num_odd > 0:
            return False
        if num_odd > 1:
            return False
        if v % 2 == 1:
            num_odd += 1
    
    return True
        