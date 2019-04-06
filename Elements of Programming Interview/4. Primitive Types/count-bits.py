# Count the number of bits set to 1 in a non-negative integer

# Tests one bit at a time from the least significant bit
# Once the bit is checked, the number is right shifted by 1, to check the next bit
# O(n) time, O(1) space

def count_bits(x):
    bits = 0
    while x:        
        bits += x & 1
        x >>= 1
    return bits

print(count_bits(12))
