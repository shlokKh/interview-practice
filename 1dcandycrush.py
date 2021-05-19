def candy_crush(line: str):
    stack = []
    ans = ""
    for c in line:
        if len(stack):
            if stack[-1][0] == c:
                stack[-1] = (c, stack[-1][1]+1)
            else:
                while len(stack) and stack[-1][1] >= 3:
                    stack.pop()
                if len(stack) and stack[-1][0] == c:
                    stack[-1] = (c, stack[-1][1]+1)
                else:
                    stack.append((c,1))
        else:
            stack.append((c, 1))
    newStack = []
    for c, n in stack:
        if n < 3:
            newStack.append((c, n))

    for c, n in newStack:
        while n > 0:
            ans += c
            n -= 1
    
    return ans
                

if __name__ == "__main__":
    assert candy_crush("aaabbbc") == "c"
    assert candy_crush("aabbbacd") == "cd"
    assert candy_crush("baaabbbabbccccd") == "abbd"
    assert candy_crush("") == ""
    assert candy_crush("bbbbbbb") == ""
    assert candy_crush("aaabbbacd") == "acd"
    assert candy_crush("ccddccdcaacabbbaaccaccddcdcddd") == ""