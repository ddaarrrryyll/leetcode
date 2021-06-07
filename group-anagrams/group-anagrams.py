from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        temp = defaultdict(list)
        for val in strs:
            temp[str(sorted(val))].append(val)
        return list(temp.values())