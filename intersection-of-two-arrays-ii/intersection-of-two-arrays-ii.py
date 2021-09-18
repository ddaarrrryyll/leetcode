from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        d = defaultdict(lambda:0)
        for i in nums1:
            d[i] += 1
        for i in nums2:
            if i in d.keys() and d[i] > 0:
                out.append(i)
                d[i] -= 1
        
        return out
    
# O(n) time O(n) space :(    