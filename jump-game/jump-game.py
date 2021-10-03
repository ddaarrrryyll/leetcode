# keep track of number of jumps needed to get to a particular index
# start from second last element of array since we are handling last element as base case
# 2,3,0,1,4
# from nums[3] to nums[4] 1 jump is  needed no matter what is in nums[3], check if nums[3] has the required number (more than 1)
# from nums[2] to nums[4] number of jumps needed has been calculated from previous step (needed=1), since nums[2] has (0<1), we increment required jumps
# from nums[1] to nums[4] required = 2, since nums[1] has (3>2), we can reset required to 1 since as long as we can reach nums[1] and jump once, we can reach nums[4]
# we just need to return whether nums[0] has enough for us to reach nums[1] or any other index that can bring us to last element


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        need = 1
        # to second last element
        for i in range(len(nums)-2, 0, -1):
            if nums[i] < need:
                need += 1
            else:
                need = 1
        return nums[0] >= need