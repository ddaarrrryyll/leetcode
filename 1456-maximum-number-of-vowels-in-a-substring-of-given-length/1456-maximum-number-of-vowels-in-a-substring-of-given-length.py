class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        
        count = 0
        for i in range(k):
            count += (s[i] in vowels)
                    
        ans = count
        for i in range(len(s) - k):
            count += (s[i + k] in vowels)
            count -= (s[i] in vowels)
            ans = count if count > ans else ans
            
        return ans
    