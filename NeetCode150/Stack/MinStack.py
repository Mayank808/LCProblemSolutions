class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        
        self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        if not self.stack:
            # raise Exception("Called top when stack is empty")
            return # can also throw error
        self.stack.pop()
        
    def top(self) -> int:
        if not self.stack:
            # or throw error
            raise Exception("Called top when stack is empty")
        
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        if not self.stack:
            # or throw error
            raise Exception("Called getMin when stack is empty")
        return self.stack[-1][1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()