class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # sum of any two sides must always be larger than the last side
        nums.sort()
        # always pick the last 3 first (largest peri)
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return sum(nums[i:i+3])
        return 0