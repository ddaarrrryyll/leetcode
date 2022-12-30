class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1: return sum(nums)
        if k == len(nums): return max(nums)
        lower, upper = max(nums), sum(nums)
        while lower < upper:
            # the amount we want is between max(nums) and sum(nums)
            mid = (lower + upper) // 2
            total, arrs = 0, 1
            for num in nums:
                if total + num <= mid:
                    total += num
                else:
                    total = num
                    arrs += 1
            # split too much, means mid is too small
            if arrs > k:
                lower = mid + 1
            else:
                upper = mid
        return upper