'''
My logic is for every level it 2^h h = the height

'''
def weave_list(l1, l2, results, prefix):
    if len(l1) == 0 or len(l2) == 0:
        result = prefix
        results.append(result + l1 + l2)
        return

    headFirst = l1.pop(0)
    print(headFirst)
    prefix.append(headFirst)
    weave_list(l1, l2, results, prefix)
    prefix.pop()
    l1.insert(0, headFirst)
    
    headSecond = l2.pop(0)
    prefix.append(headSecond)
    weave_list(l1, l2, results, prefix)
    prefix.pop()
    l2.insert(0, headSecond)




l1 = [1,2]
l2 = [3,4]
results = []
prefix = []
weave_list(l1, l2, results, prefix)
print(results)

