class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res, curEnd = 1, points[0][1]
        
        for start, end in points:
            if start > curEnd:
                res += 1
                curEnd = end
        return res