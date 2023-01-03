class MyCircularDeque:

    def __init__(self, k: int):
        if k < 1:
            raise Exception
        self.dq = [0] * k
        self.max_size = k
        self.size = 0
        self.head = 0
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.dq[self.head] = value
        else:
            self.head = (self.head-1) % self.max_size
            self.dq[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.dq[self.tail] = value
        else:
            self.tail = (self.tail+1) % self.max_size
            self.dq[self.tail] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.dq[self.head] = -1
        self.head = (self.head+1) % self.max_size
        self.size -= 1
        if self.isEmpty():
            self.tail = self.head
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.dq[self.tail] = -1
        self.tail = (self.tail-1) % self.max_size
        self.size -= 1
        if self.isEmpty():
            self.head = self.tail
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.dq[self.head]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.dq[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()