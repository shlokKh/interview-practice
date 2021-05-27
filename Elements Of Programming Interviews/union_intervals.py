from collections import namedtuple

Endpoint = namedtuple('Endpoint', ('is_closed', 'val'))

class Interval():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        if self.left.val != other.left.val:
            return self.left.val < other.left.val
        return self.left.is_closed and not other.left.is_closed


def union_intervals(intervals):
    intervals.sort()
    if len(intervals) == 0:
        return []
    result = []
    result.append(intervals[0])

    i = 1
    while i < len(intervals):
        #Case 1: The interval is intersected
        if intervals[i].left.val < result[-1].right.val or (intervals[i].left.val == intervals[i].right.val and (intervals[i].left.is_closed or result[-1].right.is_closed)):
            if intervals[i].right.val > result[-1].right.val or (intervals[i].right.val == intervals[i].right.val and (intervals[i].right.is_closed)):
                result[-1].right = intervals[i].right
        else:
            result.append(intervals[i])
        i += 1
    return result



