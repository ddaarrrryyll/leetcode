from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(lambda: [])
        for string in strs:
            temp[str(sorted(string))].append(string)
        return temp.values()