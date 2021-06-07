class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = -0x69696cafebabe
        new_max = -0x69696cafebabe
        
        for i in nums:
            new_max = max(i, new_max + i)
            if new_max > current_max:
                current_max = new_max
        return current_max