#One Away Three types of edits that can be performed on strings: insert, delete, or replace and only one edit can be made

#Space Complexity O(1)
#Time complexity O(min(len(str1), len(str2)))
def one_away(str1, str2):
    edit = False
    l1 = len(str1)
    l2 = len(str2)
    offset1 = 0
    offset2 = 0 
    if abs(l1 - l2) > 1:
        return False
    if l1 > l2:
        l = l2
    else:
        l = l1
    for i in range(0, l):
        if str1[i-offset1] != str2[i-offset2]:
            if edit:
                return False
            else:
                #Replace
                if l1 == l2:
                    edit = True
                #Insert
                elif l1 < l2:
                    edit = True
                    offset1 = 1
                #Delete
                else:
                    edit = True
                    offset2 = 1
    return True

print(one_away("pale", "ple"))
print(one_away("paless", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
print(one_away("aat", "at"))