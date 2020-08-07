#Palindrome Permutation


#Space Complexity O(n)
#Time Complexity O(n)
def palindrome_permutation(s):
    s = s.lower().replace(" ", "")
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    
    odd = False
    for v in d.values():
        if v % 2 == 1:
            if len(s) % 2 == 1 and not odd:
                odd = True
            else:
                return False

    return True

print(palindrome_permutation("Tact Cao"))