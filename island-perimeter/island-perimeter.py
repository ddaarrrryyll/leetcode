# perimeter of each cell = 4-number of neighbours

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    # print(4-self.neighbours(grid, i, j))
                    perimeter += 4-self.neighbours(grid, i, j)
        return perimeter
    
    def neighbours(self, grid, i, j) -> int:
        neighbours = 0
        neighbours = neighbours + self.util(grid, i, j+1) + self.util(grid, i, j-1) + self.util(grid, i+1, j) + self.util(grid, i-1, j)
        # print(neighbours)
        return neighbours
    
    def util(self, grid, i, j) -> int:
        try:
            if grid[i][j] == 1 and i != -1 and j != -1:
                # print(f"{i} {j} is neighbour")
                return 1
        except (IndexError):
            return 0
        return 0