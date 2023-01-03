class MyCircularQueue:

    def __init__(self, k: int):
        if k < 1:
            raise Exception
        self.queue = [0] * k
        self.head = 0
        self.tail = 0
        self.max_size = k
        self.curr_size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.queue[self.tail] = value
        self.curr_size += 1
        self.tail = (self.tail+1) % self.max_size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head+1) % self.max_size
        self.curr_size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.tail-1]

    def isEmpty(self) -> bool:
        return self.curr_size == 0 

    def isFull(self) -> bool:
        return self.curr_size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()