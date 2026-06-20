class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 0
        
    def push(self, val: int) -> None:
        diff = val - self.min if self.stack else 0
        if diff <= 0:
            self.min = val
        self.stack.append(diff)
        # print('push', self.stack, self.min)

    def pop(self) -> None:
        if self.stack and self.stack[-1]<0:
            self.min = self.min - self.stack[-1]
        # print('pop', self.stack, self.min)
        self.stack.pop()
        # print('pop', self.stack, self.min)

    def top(self) -> int:
        if self.stack and self.stack[-1]<0:
            # print('top', self.stack, self.min)
            return self.min
        else:
            # print('top', self.stack, self.min)
            return self.stack[-1] + self.min
        
    def getMin(self) -> int:
        # print('min', self.stack, self.min)
        return self.min
        
