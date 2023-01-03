class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.max_size = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            res = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = res
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.max_size:
                self.cache.popitem(last=False)
        self.cache[key] = value
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)