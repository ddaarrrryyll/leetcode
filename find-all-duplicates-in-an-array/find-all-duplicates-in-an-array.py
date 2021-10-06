# O(n) time means can't sort
# O(1) space means no new arrays

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        out = []
        while i < len(nums):
            # if nums[i] is not at it's position
            # print(nums[nums[i]-1], nums[i])
            if nums[nums[i]-1] != nums[i]:
                # swap number with number at its position if number at its position is not in the correct position
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp

            else:
                i+=1
                
            # print(nums)
            
        for i in range(len(nums)):
            if nums[i] != i+1:
                out.append(nums[i])
        return out