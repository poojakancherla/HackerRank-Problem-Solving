
# the result is multiplied by 10 everytime, before adding the next number
# 2*10 + 3 = 23, then 23*10 + 1 = 231, then 231*10 + 1 = 2311
# To get the remaining number on which we need to perform the reverse operation, just keep dividing the num by 10

def reverseDigits(x):
    result = 0
    while x:
        result = result * 10 + (x % 10)
        x = x // 10
    return result

print(reverseDigits(1132))