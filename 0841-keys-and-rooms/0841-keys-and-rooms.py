class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]
        # create adj list
        neighbours = defaultdict(lambda: [])
        for i in range(len(rooms)):
            neighbours[i] = rooms[i]
        
        def dfs(curr): 
            if visited[curr]:
                return
            else:
                visited[curr] = True
                nbs = neighbours[curr]
                if not nbs:
                    return
                for nb in nbs:
                    dfs(nb)
            
        dfs(0)
        return all(visited)