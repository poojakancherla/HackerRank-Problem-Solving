# Using Recursion
# O(2^N) time and O(N) space

# When sequence starts with 1
def getNthFib1(n):
    if n == 0: return 0
    if n == 1: return 1
    return getNthFib1(n-1) + getNthFib1(n-2)

# When sequence starts with 0
def getNthFib2(n):
    if n == 2: return 1
    if n == 1: return 0
    return getNthFib2(n-1) + getNthFib2(n-2)

print(getNthFib1(6))
print(getNthFib2(6))


# O(N) time and O(N) space
# Using Memoization
def getNthFibMem(n, memoize = {1: 0; 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1) + getNthFib(n-2)
        return memoize[n]

# O(N) time and O(1) space
# Using Iteration
def getNthFibIter(n):
    lastTwo = [0,1]
    i = 3
    while i <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        i += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
