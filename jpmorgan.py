def scrollNumbers(a, b):
    

    for n in range(a, b+1):
        digits = str(n)
        visited = set()
        for c in digits:
