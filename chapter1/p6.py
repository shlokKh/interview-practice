#String compression implement a method to perform basic string compression using the counts of repeated characters

#Space Complexity is O(1)
#Time Complexity is O(n)
def string_compression(s):
    count = 0
    ans = ""
    prev_letter = ''
    parts = []
    for c in s:
        if prev_letter != c:
            if count != 0:
                parts.append(prev_letter + str(count))
            count = 1
            prev_letter = c

        else:
            count += 1
    parts.append(prev_letter + str(count))
    ans = ''.join(parts)
    if len(ans) < len(s):
        return ans
    else:
        return s

print(string_compression("aabcccccaaa"))