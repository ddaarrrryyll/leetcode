class Solution:
    def jump(self, nums: List[int]) -> int:
        # check from the back
        dp = [inf] * len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            temp = inf
            for j in range(i+1, min(len(nums)-1, i+nums[i]) + 1):
                temp = min(temp, dp[j])
            if temp != inf:
                dp[i] = temp + 1
        return dp[0]