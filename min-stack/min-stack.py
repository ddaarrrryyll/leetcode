class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []
        
    def push(self, x: int) -> None:
        self.vals.append(x)

    def pop(self) -> None:
        self.vals.pop()

    def top(self) -> int:
        if self.vals:
            return self.vals[-1]
        else:
            return None
        
    def getMin(self) -> int:
        return min(self.vals)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()