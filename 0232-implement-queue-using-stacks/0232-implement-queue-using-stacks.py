class MyQueue:

    def __init__(self):
        self.stack_main = deque()
        self.stack_helper = deque()

    def push(self, x: int) -> None:
        self.stack_main.append(x)

    def pop(self) -> int:
        while (self.stack_main):
            self.stack_helper.append(self.stack_main.pop())
        out = self.stack_helper.pop()    
        while (self.stack_helper):
            self.stack_main.append(self.stack_helper.pop())
        return out
        
    def peek(self) -> int:
        while (self.stack_main):
            self.stack_helper.append(self.stack_main.pop())
        out = self.stack_helper[-1]
        while (self.stack_helper):
            self.stack_main.append(self.stack_helper.pop())
        return out
    
    def empty(self) -> bool:
        return len(self.stack_main) == 0 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()