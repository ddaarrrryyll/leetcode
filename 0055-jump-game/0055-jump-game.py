class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        need = 1
        for i in range(len(nums)-2, 0, -1):
            if nums[i] < need:
                need += 1
            else:
                need = 1
        return nums[0] >= need