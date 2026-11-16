# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        self.minStack.append(min(node, self.minStack[-1] if self.minStack else node))

    def pop(self):
        # write code here
        self.minStack.pop()
        return self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]
