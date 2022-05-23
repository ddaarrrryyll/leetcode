class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        DP = [[0] * (n+1) for _ in range(m+1)]
        count_0_1 = []
        for binary in strs:
            count_0_1.append((binary.count('0'), binary.count('1')))
        
        # if x_count is more than m or n, we skip it automatically
        # if we have no allowance left, we see if taking the new binary will give a bigger result
        for zero_count, one_count in count_0_1:
            for i in range(m, zero_count - 1, -1):
                for j in range(n, one_count - 1, -1):
                    DP[i][j] = max(DP[i][j], 1 + DP[i-zero_count][j-one_count])
        
        return DP[-1][-1]