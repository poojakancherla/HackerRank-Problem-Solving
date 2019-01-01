# construct a stack with tuples of integers and their roman symbol
# arranged the integers from lower value to higher value, such that roman number can form correctly by using the last element of the stack
# while there is number, if it is greater than or equal to last element of statck, subtract that value from number and
# add its corresponding roman value to result
# repeat this until the number becomes smaller than the last stack element. In this case, pop it
# Now compare the number with the new last element of stack
# Keep repeating until the number becomes zero and result becomes number(roman number)

def intToRoman(num):
    stack = [(1,'I'), (4,'IV'), (5,'V'), (9,'IX'), (10,'X'), (40,'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400,'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
    result = ''
    while(num):
        if num >= stack[-1][0]:
            num -=stack[-1][0]
            result += stack[-1][1]
        else:
            stack.pop()

    return result

print(intToRoman(1994))
