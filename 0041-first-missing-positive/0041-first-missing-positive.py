class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # we can use len(nums)+1 as a flag and mod nums[i] to get the og value back
        # cleaning
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0
        
        # we are using the index as the positive value to return
        for i in range(n):
            og = nums[i] % (n+1)
            if 0 < og <= n:
                nums[og-1] += n+1
        
        for i in range(n):
            if nums[i] < n+1:
                return i+1
        
        return len(nums)+1