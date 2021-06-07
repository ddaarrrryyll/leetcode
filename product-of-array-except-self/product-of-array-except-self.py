class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return
        
        i, temp = 1, 1
        res = [1 for i in range(n)]
        
        for i in range(n):
            res[i] = temp
            temp *= nums[i]
            
        temp = 1
        
        for i in range(n - 1, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        return res