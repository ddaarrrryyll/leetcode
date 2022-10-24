class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        
        for word in arr:
            chars = set(word)
            if len(chars) < len(word): continue
            
            temp = []
            for prev in dp:
                if not chars & prev:
                    temp.append(chars | prev)
            dp.extend(temp)
            # print(dp)
        
        return max(map(len, dp))