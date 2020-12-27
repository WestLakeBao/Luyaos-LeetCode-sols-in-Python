# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
# The integer division should truncate toward zero.

class Solution(object):
    def calculate(self, s):
        s += '+0'
        result = 0
        stack = []
        previous_operator = '+'
        for char in s:
            if char.isdigit():
                result = 10 * result + int(char)
            elif not char.isspace():
                if previous_operator == '+':
                    stack.append(result)
                elif previous_operator == '-':
                    stack.append(-result)
                elif previous_operator == '*':
                    stack.append(stack.pop() * result)
                else:
                    stack.append(int(stack.pop() / result))
                previous_operator, result = char, 0
        return sum(stack)