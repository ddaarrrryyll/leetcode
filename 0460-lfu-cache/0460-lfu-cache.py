class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.k2f = {}
        self.f2k = defaultdict(lambda: deque())
        self.max_size = capacity

    def get(self, key: int) -> int:
        try:
            res = self.cache[key]
            freq = self.k2f[key]
            self.k2f[key] += 1
            self.f2k[freq].remove(key)
            self.f2k[freq+1].append(key)
            return res
        except KeyError:
            return -1
        
    
    def put(self, key: int, value: int) -> None:
        if self.max_size < 1: return
        if key in self.cache:
            freq = self.k2f[key]
            self.k2f[key] += 1
            self.f2k[freq].remove(key)
            self.f2k[freq+1].append(key)
        else:
            if len(self.cache) == self.max_size:
                for i in range(1, max(self.f2k.keys())+1):
                    if self.f2k[i]:
                        to_replace = self.f2k[i].popleft()
                        del self.k2f[to_replace]
                        del self.cache[to_replace]
                        break
        
            self.k2f[key] = 1
            self.f2k[1].append(key)
            
        self.cache[key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)