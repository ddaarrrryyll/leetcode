class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # create adj list
        neighbours = defaultdict(lambda: [])
        for edge in edges:
            curr, neighbour = edge
            neighbours[curr].append(neighbour)
            neighbours[neighbour].append(curr)
        
        # print(neighbours)
        # bfs
        visited = [False] * n
        def bfs(s, d, visited, neighbours):
            # print(f'at {s}')
            if s == d:
                return True
            if visited[s] or not neighbours[s]:
                return False
            visited[s] = True
            for neighbour in neighbours[s]:
                if bfs(neighbour, d, visited, neighbours): 
                    return True
                else: 
                    continue
            return False
        
        return bfs(source, destination, visited, neighbours)