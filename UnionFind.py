# also known as disjoint set union

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
        return True
      
      
