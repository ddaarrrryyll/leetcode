class Allocator:

    def __init__(self, n: int):
        self.max_size = n
        # {idx: mID, size}
        self.memtable = {}
        
    def allocate(self, size: int, mID: int) -> int:
        avail = 0
        i = 0
        while i < self.max_size:
            if i not in self.memtable:
                avail += 1
            else:
                i += self.memtable[i][1]
                if avail < size:
                    avail = 0
                    continue
            if avail >= size:
                self.memtable[i+1-avail] = (mID, size)
                return i+1-avail
            i += 1
            
        return -1

    def free(self, mID: int) -> int:
        count = 0
        to_del = []
        for idx, pair in self.memtable.items():
            if mID == pair[0]:
                to_del.append(idx)
                count += pair[1]
        for i in to_del:
            del self.memtable[i]
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)