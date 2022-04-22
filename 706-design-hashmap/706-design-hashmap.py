class MyHashMap:

    def __init__(self):
        self.l = []

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            self.l.append([key, value])
        else:
            for pair in self.l:
                if pair[0] == key: pair[1] = value

    def get(self, key: int) -> int:
        # you can prolly do binary search here
        for pair in self.l:
            if pair[0] == key: return pair[1]
        return -1

    def remove(self, key: int) -> None:
        for idx in range(len(self.l)):
            if self.l[idx][0] == key:
                self.l.pop(idx)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)