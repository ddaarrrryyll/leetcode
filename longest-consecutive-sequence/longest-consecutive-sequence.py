class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s_nums = sorted(nums)
        print(s_nums)
        longest = 1
        count = 1
        for i, n in enumerate(s_nums):
            
            if i == len(s_nums) - 1:
                break
            if s_nums[i+1] == n:
                continue
            if s_nums[i+1] == n + 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 1
        return longest