#Can't use additional data structures
def is_unique1(s):
    for c in range(0, len(s)):
        for i in range(c, len(s)):
            if s[c] == s[i]:
                return False
    
    return True

'''
Time complexity = O(n^2) n is the length of the string
Space complexity = O(1) just the parameter
'''

#Using additional datastructures
def is_unique2(s):
    letters = set()
    for c in s:
        if c in letters:
            return False
        letters.add(c)
    return True

'''
Time complexity = O(n)
Space Complexity = O(n)
'''

def is_unique3(s):
    letters = [0]*26
    for c in s:
        letters[int(c)-97] += 1
    
    for n in letters:
        if n > 1:
            return False
    return True

'''
Time complexity = O(n)
Space complexity = O(1)
'''

def is_unique4(s):
    checker = 0
    for c in s:
        bit =  ord(c) - ord('a')

        if (checker & 1 << bit) > 0:
            return False
        
        checker = checker | 1 << bit
    return True
print(is_unique4("apless"))