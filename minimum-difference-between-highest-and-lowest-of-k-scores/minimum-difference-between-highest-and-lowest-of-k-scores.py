class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        out = float("inf")
        i = 0
        while i + k-1 < len(nums):
            if nums[i+k-1] - nums[i] < out:
                out = nums[i+k-1] - nums[i]
                
            i+=1
        return out