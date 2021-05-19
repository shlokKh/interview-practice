
def partition(start, end, a):
    pivot_idx = start
    pivot = a[start]

    while start < end:
        while start < len(a) and a[start] <= pivot:
            start += 1
        while end > 0 and a[end] > pivot:
            end -= 1
        if start < end:
            a[start], a[end] = a[end], a[start]

    a[end], a[pivot_idx] = pivot, a[end]

    return end
def quick_sort(start, end, a):
    if start < end:
        p = partition(start, end, a)
        quick_sort(0, p-1, a)
        quick_sort(p+1, end, a)


array = [ 10, 7, 8, 9, 1, 5  ]
quick_sort(0, len(array) - 1, array)
print(array)
