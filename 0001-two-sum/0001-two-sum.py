class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            pair = target - num
            try:
                if dic[pair] != None:
                    return [idx, dic[pair]]
            except:
                dic[num] = idx
        