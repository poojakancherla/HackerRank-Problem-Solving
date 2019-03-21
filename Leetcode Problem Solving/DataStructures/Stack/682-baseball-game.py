# https://leetcode.com/problems/baseball-game/description/

def calPoints(ops):
    stack = []

    for string in ops:
        if string == "C": del stack[-1]
        elif string == "D": stack.append(2 * stack[-1])
        elif string == "+": stack.append(stack[-1] + stack[-2])
        else: stack.append(int(string))

    return sum(stack)

print(calPoints(["5","-2","4","C","D","9","+","+"]))
