from collections import defaultdict

def mergeIntervals(intervals):
    graph = defaultdict(lambda: [])
    def overlap(a, b):
        return a[0] <= b[1] and b[0] <= a[1]
    def buildGraph():
        for i, interval in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if overlap(interval, intervals[j]):
                    graph[tuple(interval)].append(tuple(intervals[j]))
                    graph[tuple(intervals[j])].append(tuple(interval))
        return graph
    def 

    return buildGraph()

print(mergeIntervals([[1,5], [4,7], [6,10], [15,17], [16,20]]))