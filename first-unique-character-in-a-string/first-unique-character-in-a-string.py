class Solution:
    def firstUniqChar(self, s: str) -> int:
        matched = [0] * len(s)
        for i in range(len(s)):
            # skip if has been matched 
            if matched[i]:
                continue
            
            flag = 0
            for j in range(i+1, len(s)):
                # if anything after i is matched, we set it in matched array so that we can skip them afterwards
                if s[i] == s[j]:
                    matched[j] = 1
                    flag = 1
                    
            if not flag:
                return i
            
        return -1