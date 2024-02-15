class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        r, c = len(heightMap), len(heightMap[0])
        heap = []
        directions = ((-1,0), (1,0), (0, -1), (0, 1))
        
        for i in range(r):
            for j in range(c):
                # push outer edge into heap
                if i in (0, r-1) or j in (0, c-1):
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1 # mark as visited
        res = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if x < 0 or x >= r or y < 0 or y >= c or heightMap[x][y] == -1:
                    continue
                res += max(0, h-heightMap[x][y])
                heapq.heappush(heap, (max(h, heightMap[x][y]), x, y))
                heightMap[x][y] = -1
        return res