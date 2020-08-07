#Implement an algorithm to determine if a string has all unique characters

#O(n) Space
#O(n) Time
#n = length of the string
def isUnique1(string):
    dict = {}
    for c in string:
        if c in dict:
            return False
        else:
            dict[c] = 1
    return True
print(isUnique1("abdsdas"))
print(isUnique1("abcdfe"))

#Assuming character set is in ascii

#Space O(1) constant space used to store characters
#Time O(n)
def isUnique2(string):
    arr = [0]*128
    
    for c in string:
        if arr[ord(c)] == 0:
            arr[ord(c)] = 1
        else:
            return False
    return True
print(isUnique2("abdsdas"))
print(isUnique2("abcdfe"))

#Assuming we cannot use any data structures

#Space O(1)
#Time O(n)
def isUnique3(string):
    string = sorted(string)
    for c in range(0, len(string)-1):
        if string[c] == string[c+1]:
            return False
    return True
print(isUnique3("abdsdas"))
print(isUnique3("abcdfe"))