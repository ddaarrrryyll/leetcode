class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # dijkstra
        # building graph
        graph = defaultdict(list)
        for source, dest, cost in times:
            graph[source].append((dest, cost))
            
        # minheap, visited set, ans to return
        queue = [(0, k)]
        visited = set()
        furthest_cost = 0
        
        # visit all nodes
        while queue:
            cost, node = heapq.heappop(queue)
            if node in visited: continue
                
            visited.add(node)
            
            furthest_cost = max(furthest_cost, cost)
            
            neighbours = graph[node]
            for neighbour in neighbours:
                neighbour_node, neighbour_cost = neighbour
                if neighbour_node not in visited:
                    curr_cost = cost + neighbour_cost
                    heapq.heappush(queue, (curr_cost, neighbour_node))
        
        # if all nodes visited, return furthest cost
        return furthest_cost if len(visited) == n else -1