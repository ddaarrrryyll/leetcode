class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        right = None
        count = 0
        
        for interval in intervals:
            i_left, i_right = interval
            # if is first iteration or if curr's lower bound >= right we replace right
            if right == None or i_left >= right:
                right = i_right
                continue
            
            # if curr's lower bound < right we have to remove one, if curr's upper bound < right we want to take it (greedy)
            if i_left < right:
                if i_right < right:
                    right = i_right
                count += 1
        return count