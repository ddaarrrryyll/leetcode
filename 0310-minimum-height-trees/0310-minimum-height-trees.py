class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1: return [0]
        
        adj_list = defaultdict(lambda: set())
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
            
        leaves = [i for i in range(n) if len(adj_list[i]) == 1]
        
        print(leaves)
        
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            while leaves:
                leaf = leaves.pop()
                neighbour = adj_list[leaf].pop()
                adj_list[neighbour].remove(leaf)
                
                
                if len(adj_list[neighbour]) == 1:
                    newLeaves.append(neighbour)
                    
            leaves = newLeaves
            
        return leaves