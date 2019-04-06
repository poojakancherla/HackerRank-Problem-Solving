# One way to solve this is by counting the number of 1s and then if it is divisible by 2 -> return 0, if not -> return 1


# In this method, no need of storing the number of 1s. We bitwise-XOR the result every time. This is O(n) time
def parity(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
    
# print(parity(3))

# In the next method, we use a bit-fiddling trick to erase the lowest set bit. This gives O(k) time
def parity2(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x-1
    return result
print(parity2(11))


