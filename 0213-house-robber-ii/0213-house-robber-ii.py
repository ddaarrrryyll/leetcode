class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            rob1, rob2 = 0, 0
            for house in nums:
                newRob = max(house + rob1, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(helper(nums[:-1]), helper(nums[1:]))