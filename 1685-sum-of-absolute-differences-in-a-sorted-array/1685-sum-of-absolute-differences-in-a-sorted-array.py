class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        res = []
        i = 0
        leftWindow = 0
        rightWindow = sum(nums[i:])
        n = len(nums)
        while i < n:
            rightWindow -= nums[i]
            
            left = nums[i] * i - leftWindow
            right = rightWindow - nums[i] * (n-i-1)
            res.append(left + right)
            leftWindow += nums[i]
            i += 1
            
        return res