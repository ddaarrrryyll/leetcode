class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n+1))
    
    def find(self, x: int) -> int:
        # while parent of x is not itself
        if self.parent[x] != x:
            # find the parent of parent[x]
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def join(self, x: int, y: int):
        parent_x = self.find(x)
        parent_y = self.find(y)
        self.parent[parent_x] = parent_y
        
    def getParents(self):
        return self.parent
        
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adj_l = defaultdict(lambda: [])
        for dislike in dislikes:
            adj_l[dislike[0]].append(dislike[1])
            adj_l[dislike[1]].append(dislike[0])
        
        
        uf = UnionFind(n)
        for person in range(1, n+1):
            for hater in adj_l[person]:
                # if they curr and the hater share the same parent (in the same set) return false
                if uf.find(person) == uf.find(hater): return False
                # we can group the haters of curr person together
                uf.join(adj_l[person][0], hater)
                
        return True