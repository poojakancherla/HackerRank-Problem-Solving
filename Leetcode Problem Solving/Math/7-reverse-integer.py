def reverse_int(num):
    if num < 0: ans = -1 * int(str(num)[1:][::-1])
    else: ans = int(str(num)[::-1])
    return 0 if abs(ans) > (2**31 -1) else ans
    
print(reverse_int(-445))