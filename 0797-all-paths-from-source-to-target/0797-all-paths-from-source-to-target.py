class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        out = []
        self.bfs(graph, 0, len(graph)-1, [], [], out)
        return out
        
    def bfs(self, graph, curr, target, visited, path, out):
        path.append(curr)
        if curr == target:
            return path

        for neighbour in graph[curr]:
            subpath = self.bfs(graph, neighbour, target, visited, path, out)
            if subpath:
                out.append(subpath.copy())
            path.pop()