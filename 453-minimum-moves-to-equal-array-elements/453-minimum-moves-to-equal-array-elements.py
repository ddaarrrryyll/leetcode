class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        return sum([v - min_val for v in nums])