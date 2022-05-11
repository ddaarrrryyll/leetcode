from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(lambda: 0)
        for i in nums:
            dic[i] += 1
            if dic[i] > 1: return True
        
        return False