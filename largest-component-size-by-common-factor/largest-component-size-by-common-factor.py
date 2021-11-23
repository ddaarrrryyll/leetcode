class UnionFind:
    def __init__(self, n : int):
        self.parent = list(range(n+1))
        
    def find(self, x : int) -> int:
        # while parent of x is not itself
        if self.parent[x] != x:
            # find the parent of parent[x]
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    def union(self, x : int, y : int):
        parent_x = self.find(x)
        parent_y = self.find(y)
        # union both
        self.parent[parent_x] = parent_y
        

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        out = 0
        uf = UnionFind(max(nums))
        count = Counter()
        
        for num in nums:
            # factor should never be greater than sqrt num + 1
            for factor in range(2, int(sqrt(num) + 1)):
                if num % factor == 0:
                    # num join both factors if factor is factor of num (eg. for 6, join with 3 and 2)
                    uf.union(num, factor)
                    uf.union(num, num//factor)
                    
        for num in nums:
            parent_num = uf.find(num)
            count[parent_num] += 1
            out = max(out, count[parent_num])
            
        return out