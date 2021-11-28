class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        out = []
        self.dfs(graph, 0, path, out)
        return out
    
    # modified dfs which searches all possible path
    def dfs(self, graph, node, path, out):
        
        # print(f"now at node: {node}")
        path.append(node)
        # print(f"{path=}")
        
        # if reached the end
        if node == len(graph) - 1:
            return path
        
        for neighbour in graph[node]:
            temp = self.dfs(graph, neighbour, path, out)
            # print(f"{temp = }")
            if temp:
                out.append(temp.copy())
                # print(f"{out=}")
            path.pop()
    