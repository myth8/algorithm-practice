# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, node):
        # write code here
        self.inStack.append(node)

    def pop(self):
        if self.outStack:
            return self.outStack.pop()
        while self.inStack:
            self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self):
        if self.outStack:
            return self.outStack[-1]
        while self.inStack:
            self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        return not self.inStack and not self.outStack
