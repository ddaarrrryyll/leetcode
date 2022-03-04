class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        
        nums.sort()
        n = len(nums)
        # possible combinations:
        # 0,1,2,3 (...) n-4, n-3, n-2, n-1
        # n-4 - 0 | n-3 - 1 | n-2 - 2 | n-1 - 3|
        
        ans = float('inf')
        for i in range(4):
            ans = min(ans, nums[-4+i] - nums[i])
            
        return ans