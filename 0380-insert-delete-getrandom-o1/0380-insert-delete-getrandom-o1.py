class RandomizedSet:

    def __init__(self):
        self.hash_map = defaultdict(lambda: None)
        self.vals = []
        
    def insert(self, val: int) -> bool:
        if not self.hash_map[val]:
            self.hash_map[val] = True
            self.vals.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.hash_map[val]:
            self.hash_map[val] = False
            self.vals.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()