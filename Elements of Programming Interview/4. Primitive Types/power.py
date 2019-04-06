#  x is base, y is power
#  O(n) time
def power(x, y):
    result = 1.0
    power = y
    if y < 0: 
        power, x = -power, 1/x

    while power:
        if power & 1: # If the power is odd, multiply just x
            result *= x
        x, power = x*x, power >> 1
    
    return result

print(power(2,3))