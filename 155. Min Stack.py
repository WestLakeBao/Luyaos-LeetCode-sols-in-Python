# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        if self.minStack == [] or self.minStack[-1][0] > x:
            self.minStack.append((x, 1))
        elif self.minStack[-1][0] == x:
            self.minStack[-1] = (x, self.minStack[-1][1] + 1)

    def pop(self):
        self.stack.pop()
        top = self.stack[-1]
        if self.minStack[-1][0] == top:
            if self.minStack[-1][1] > 1:
                self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
            else:
                self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1][0]

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # Returns -3.
    minStack.pop()
    minStack.top()  # Returns 0.
    print(minStack.getMin())  # Returns -2.