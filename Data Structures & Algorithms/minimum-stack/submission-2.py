class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
        else:
            self.stack.append(val-self.min)
        self.min = min(self.min, val)        

    def pop(self) -> None:

        diff = self.stack.pop()

        if diff < 0:

            # restore previous minimum

            self.min = self.min - diff

        if not self.stack:

            self.min = float('inf')
        

    def top(self) -> int:
        if self.stack and self.stack[-1]>0:
            return self.stack[-1] + self.min
        else:
            return self.min
        
    def getMin(self) -> int:
        return self.min
        
