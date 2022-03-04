class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        # simulation, max rows = 100
        Tower = [[0] * i for i in range(1, 102)]
        Tower[0][0] = poured
        for row in range(query_row+1):
            for col in range(row+1):
                
                # overflow on both sides = amount poured - 1 divided by 2 from both sides
                overflow = (Tower[row][col]-1)/2
                # if overflow > 0, overflow into next row 
                if overflow > 0:
                    Tower[row+1][col] += overflow
                    Tower[row+1][col+1] += overflow
                    
        return min(1, Tower[query_row][query_glass])