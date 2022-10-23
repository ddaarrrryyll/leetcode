class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lib = [1]
        lib.extend([0 for i in range(1, n+1)])
        for num in nums:
            if lib[num]:
                dupe = num
            lib[num] = 1
        missing = lib.index(0)
        return dupe, missing