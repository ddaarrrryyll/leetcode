class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        curr_max = 0
        total = 0
        prev = 'z'
        
        for i in range(len(colors)):
            curr_cost = neededTime[i]
            curr_col = colors[i]
            if curr_col == prev: curr_max = max(curr_max, curr_cost)
            else:
                total += curr_max
                curr_max = curr_cost
            prev = colors[i]
        total += curr_max
        
        return sum(neededTime) - total