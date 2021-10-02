class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # knight reaches princess with at least 1hp
        DP = [[0 for _ in range(len(dungeon[0]))] for __ in range(len(dungeon))]

        
        # bottom to top
        for i in range(len(dungeon)-1, -1, -1):
            # right to left
            for j in range(len(dungeon[0])-1, -1, -1):
                
                # princess cell
                if i == len(dungeon)-1 and j == len(dungeon[0])-1:
                    if dungeon[i][j] >= 0:
                        DP[i][j] = 0
                    else:
                        DP[i][j] = dungeon[i][j]
                    continue
                    
                else:
                    # if magic orbs or 0
                    if dungeon[i][j] + self.getAdjMax(i, j, DP) >= 0:
                        DP[i][j] = 0
                    else:
                        DP[i][j] = dungeon[i][j] + self.getAdjMax(i, j, DP)
                
        print(DP)
        return abs(DP[0][0])+1
    
    def getAdjMax(self, i, j, DP):
        try:
            right = DP[i][j+1]
        except (IndexError):
            right = -float('inf')
        try:
            bot = DP[i+1][j]
        except (IndexError):
            bot = -float('inf')
        
        return max(right, bot)