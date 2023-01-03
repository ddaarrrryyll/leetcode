class MyLinkedList:

    class LLNode:
        def __init__(self, val):
            self.val = val
            self.next = None
    
    def __init__(self):
        self.size = 0
        self.llhead = None
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.llhead

        for _ in range(0, index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        node = self.LLNode(val)
        curr = self.llhead
        
        if index <= 0:
            node.next = curr
            self.llhead = node
        else:
            for _ in range(index-1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
        
        self.size += 1
            

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.llhead = self.llhead.next
            self.size -= 1
            return
        
        if 0 <= index < self.size:
            i = 0
            curr = self.llhead
            while i < index-1:
                curr = curr.next
                i += 1
            curr.next = curr.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)