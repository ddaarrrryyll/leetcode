class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        out = []
        for i in range(1, len(intervals)):
            l1 = intervals[i][0]
            r1 = intervals[i][1]
            if l1 <= right:
                if right < r1:
                    right = r1
                else:
                    continue
            else:
                out.append([left, right])
                left = l1
                right = r1
        out.append([left, right])
        return out
            