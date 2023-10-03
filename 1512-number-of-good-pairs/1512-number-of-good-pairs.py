class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
            count += num_map[num] - 1
        return count