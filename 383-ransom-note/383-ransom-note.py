class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_counter = Counter(ransomNote)
        mg_counter = Counter(magazine)

        for k,v in rn_counter.items():
            if v > mg_counter[k]:
                return False
            
        return True