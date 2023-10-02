class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        # if (nums[-1] - nums[0]) < len(nums)-1:
        #     count = len(nums)-1 - nums[0]
        #     nums[-1] += count
        # print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
                nums[i] += 1
            elif nums[i] < nums[i-1]:
                diff = nums[i-1]-nums[i]+1
                count += diff
                nums[i] += diff
            # print(nums)
                
        return count