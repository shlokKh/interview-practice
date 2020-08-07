#String Rotation

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    for c in range(len(s1)):
        if s1[c] == s2[0]:
            return s1[c:] in s2
    
    return False

print(string_rotation("waterbottle", "erbottlewat"))