import collections
def reorderArray(employees, order):

    graph = collections.defaultdict(list)
    indegree = collections.Counter()
    output=[]
    for job,boss in order:
        graph[boss].append(job)
        indegree[job]+=1

    print(graph)
    print(indegree)
    start=[k for k in graph if indegree[k]==0]

    q=collections.deque(start)
    output=[]

    d = collections.defaultdict(list)
    for name, rank in employees:
        d[rank].append(name)

    while q:
        currBoss=q.popleft()
        output+=[(x,currBoss) for x in d[currBoss]]
        for emps in graph[currBoss]:
            indegree[emps]-=1
            if indegree[emps]==0:
                q.append(emps)

    return(output[::-1])



employees=[('John', 'Manager'), ('Sally', 'CTO'), ('Sam', 'CEO'), ('Drax', 'Engineer'), ('Bob', 'CFO'), ('Daniel', 'Engineer')]
order=[['CTO', 'CEO'], ['Manager', 'CTO'], ['Engineer', 'Manager'], ['CFO', 'CEO']]
print(reorderArray(employees, order))