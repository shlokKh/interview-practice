# URLify Write a method to replace all spaces in a string with %20. You may assume that the string has sufficient space at the end to hold the additional acharacters, and that you are given the "true length of the string."

#Space = O(1)
#Time = O(1)
def URLify(string, length):
    count = 0
    difference = len(string)-length
    print(difference)
    for i in range(length-1, 0, -1):
        if string[i] == ' ':
            difference -=2
            string[i+difference] = "%"
            string[i+1+difference] = "2"
            string[i+2+difference] = "0"

        else:
            string[i+difference] = string[i]

    return string


print(URLify(["M", "r", " ", "J", "o","h","n"," ", "S", "m", "i","t", "h"," ", " ", " ", " "], 13))