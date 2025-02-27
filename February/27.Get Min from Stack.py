class Solution:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.main_stack:
            top = self.main_stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def peek(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]
        return -1

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return -1
