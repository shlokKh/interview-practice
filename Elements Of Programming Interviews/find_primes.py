'''
O(n^2) time complexity because worst case we iterate n times in the inner loop however factors are in two pairs so we only have to check half
so the half would be sqrt(n)
'''
import math
def all_primes(n):
    primes = []
    if n > 2:
        primes.append(2)
    for i in range(2, n):
        j = 2
        prime = True
        while j <= math.ceil(math.sqrt(i)):
            if i % j == 0:
                prime = False
                break
            j += 1
        if prime:
            primes.append(i)

    return primes


print(all_primes(18))
