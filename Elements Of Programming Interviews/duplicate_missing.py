def find_duplicate_and_missing(a):
    total = sum(a)
    n = len(a)
    expected_sum = ((n*(n-1))/2)
    duplicate = expected_sum - total
    missing = ((n*(n-1))/2) - (total - duplicate)

    return duplicate, missing

print(find_duplicate_and_missing([5,3,0,1,2,5]))