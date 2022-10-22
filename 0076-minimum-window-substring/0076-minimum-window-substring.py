class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""
        
        left, right = 0, 0
    
        counter_t = Counter(t)    
        unique_count_t = len(counter_t)
        
        done = 0
        
        counter_window = defaultdict(lambda: 0)
                         #len, idx , idx
        smallest_window = inf, left, right
        
        while right < len(s):
            char = s[right]
            counter_window[char] += 1
            
            if char in counter_t and counter_window[char] == counter_t[char]:
                done += 1
            
            while left <= right and done == unique_count_t:
                char = s[left]
                
                if right - left + 1 < smallest_window[0]:
                    smallest_window = right-left+1, left, right
                    
                counter_window[char] -= 1
                if char in counter_t and counter_window[char] < counter_t[char]:
                    done -= 1
                
                left += 1
            right += 1
        return "" if smallest_window[0] == inf else s[smallest_window[1] : smallest_window[2] + 1]