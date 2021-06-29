class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        le = matrix[0][0]
        ri = matrix[-1][-1]
        
        while le < ri:
            mid = (le + ri) // 2
            idx = 0
            for row in matrix:
                # print(f"bisect {bisect.bisect(row, mid)}, {row}")
                idx += bisect.bisect(row, mid)               
            if idx < k:
                le = mid + 1
            else:
                ri = mid
                
        return le