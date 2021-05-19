from functools import lru_cache
@lru_cache(maxsize=None)
def count(a, b, m, n):  

    if ((m == 0 and n == 0) or n == 0):  
        return 1

    if (m == 0): 
        return 0
  
    if (a[m - 1] == b[n - 1]):  
        return (count(a, b, m - 1, n - 1) + 
                count(a, b, m - 1, n))  
    else: 
          
        return count(a, b, m - 1, n)

def stringSubsequences(s1, s2):
    return count(s1, s2, len(s1), len(s2)) 


print(stringSubsequences('ABCBABC', 'ABC'))

from collections import defaultdict
def internationalFriends(languages, peopleSpeak, friendList, n):
    graph = defaultdict(lambda : set())
    cannotCommunicate = set()
    def build_graph():
        for f in friendList:
            graph[f[0]].add(f[1])
            graph[f[1]].add(f[0])

            if not (peopleSpeak[f[0]] & peopleSpeak[f[1]]):
                cannotCommunicate.add((f[0], f[1]))
    '''
    Given a language how many people have to learn the language to meet n
    '''
    def numberOfPeopleToLearnLanguage(language):
        for person in cannotCommunicate():
            for i in range(n):
                





