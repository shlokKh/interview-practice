def missingWords(s, t):
    sequence = t.split(' ')
    idx = 0
    ans = []
    for w in s.split():
        if idx < len(sequence) and w != sequence[idx]:
            ans.append(w)
        elif idx > len(sequence):
            ans.append(w)
        else:
            idx += 1
    
    return ' '.join(ans)

#print(missingWords("I like eating cheese do you like cheese", "like cheese"))

from collections import defaultdict
def findSubstrings(s: str) -> str:
    i, j, k = 0, 1, 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    beginnings = []
    occurences = defaultdict(lambda: [])
    min_vowel = 'z'
    max_vowel = 'a'
    for i in range(len(s)):
        if s[i] in vowels:
            occurences[s[i]].append(i)
            min_vowel = min(min_vowel, s[i])
            max_vowel = max(max_vowel, s[i])
    
    orderOfEntryPoints = []
    for c in 'aeiou':
        for idx in occurences[c]:
            orderOfEntryPoints.append(idx)
    
    min_str = None
    for idx in orderOfEntryPoints:
        j = idx + 1
        while j < len(s) and s[j] in vowels:
            j += 1

        if j < len(s):
            if not min_str:
                min_str = s[idx:j+1]
            else:
                if s[idx:j+1] > min_str:
                    break
                min_str = s[idx:j+1]

    max_str = None

    for idx in reversed(orderOfEntryPoints):
        j = len(s) - 1
        while j >= 0 and s[j] in vowels:
            j -= 1
        if j >= 0:
            if not max_str:
                max_str = s[idx:j+1]
            else:
                if s[idx:j+1] < max_str:
                    break
                max_str = s[idx:j+1]
    
    print(min_str)
    print(max_str)

    return min_str, max_str

findSubstrings("acccccccccccaaaaaaaaaaaaaaaaa")
