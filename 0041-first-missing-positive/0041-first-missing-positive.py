class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # # with linear space
        # temp = defaultdict(lambda: None)
        # for idx, num in enumerate(nums):
        #     if num > 0:
        #         temp[num] = 1
        # print(temp)
        # i = 1
        # while temp[i]:
        #     i += 1
        # return i
    
        # with constant space
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = 0
        
        for i in range(len(nums)):
            # get back the original nums[i] value
            og = nums[i] % (len(nums)+1)
            # if this og is valid, we tag the previous with (len(nums)+1)
            if 1 <= og <= len(nums):
                nums[og - 1] += len(nums) + 1
        
        # if nums[i] <= len(nums), means we never added len(nums)+1 to it aka did not meet it's +1
        for i in range(len(nums)):
            if nums[i] <= len(nums):
                return i+1
        
        return len(nums)+1