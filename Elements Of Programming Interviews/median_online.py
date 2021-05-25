import heapq


def find_median(sequence):
    medians = []
    min_heap = []
    max_heap = []
    add_to_max = 0
    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        
        medians.append((-max_heap[0] + min_heap[0]) / 2) if len(max_heap) == len(min_heap) else medians.append(min_heap[0])

    return medians

print(find_median([1,0,3,5,2,0,1]))