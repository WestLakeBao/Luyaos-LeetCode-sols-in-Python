# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        left = '({['
        right = ')}]'
        stack = []
        for bracket in s:
            if bracket in left:
                stack.append(bracket)
            else:
                if not stack or left.find(stack.pop()) != right.find(bracket):
                    return False
        return not stack


if __name__ == '__main__':
    print(Solution().isValid("()"))  # True
    print(Solution().isValid("()[]{}"))  # True
    print(Solution().isValid("(]"))  # False
    print(Solution().isValid("([)]"))  # False
    print(Solution().isValid("{[]}"))  # True