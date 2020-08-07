#Check Permutation Given two strings, write  amethod to decide if one is a permutation of the other

#Space 2*n O(n)
#Time O(n)
def check_permutation1(str1, str2):
    if len(str1) != len(str2):
        return False
    d1 = {}
    d2 = {}
    
    for i in range(len(str1)):
        if str1[i] in d1:
            d1[str1[i]] += 1
        else:
            d1[str1[i]] = 1

        if str2[i] in d2:
            d2[str2[i]] += 1
        else:
            d2[str2[i]] = 1
    

    for c in str1:
        if c in d2 and d2[c] == d1[c]:
            continue
        else:
            return False
    return True

print(check_permutation1("abc", "cab"))

print(check_permutation1("bac", "dab"))

#A worse solution would have been to sort both of the strings and then see if the words match up
#This is worse because it is an O(n*log(n)) time solution, but uses O(1) space (no additional data structures)

    
