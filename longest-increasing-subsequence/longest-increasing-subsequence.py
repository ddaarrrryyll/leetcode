class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for right in range(len(nums)):
            for left in range(right):
                # print(f"{left = } {nums[left] = } {nums[right] = }")
                # if current number is bigger than the left and the size (dp[right]) is still less than the left one, increment the size
                if nums[right] > nums[left] and dp[right] < dp[left] + 1:
                    dp[right] = dp[left] + 1
                    # print("ADDING")
            # print(dp)
        return max(dp)