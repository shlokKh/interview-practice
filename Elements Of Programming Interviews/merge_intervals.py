def merge_intervals(a, to_add):
    new_schedule = []
    i = 0

    #interval does not intersect
    while i < len(a) and a[i][1] < to_add[0]:
        new_schedule.append(a[i])
        i += 1
    
    while i < len(a) and a[i][0] <= to_add[1]:
        to_add[0] = min(a[i][0], to_add[0])
        to_add[1] = max(a[i][1], to_add[1])
        i += 1
    
    return new_schedule + [to_add] + a[i:]

print(merge_intervals([[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]], [1,8]))
    
