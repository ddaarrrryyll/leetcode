class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1
        currMax = 1
        out = nums[0]
        
        for num in nums:
            vals = (num, num * currMax, num * currMin)
            currMin = min(vals)
            currMax = max(vals)
            
            out = max(out, currMax)
            
        return out