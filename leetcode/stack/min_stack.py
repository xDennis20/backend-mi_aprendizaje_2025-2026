class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, value: int) -> None:
        if not self.stack_min or value <= self.stack_min[-1]:
            self.stack_min.append(value)
        self.stack.append(value)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.stack_min[-1]:
            self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]