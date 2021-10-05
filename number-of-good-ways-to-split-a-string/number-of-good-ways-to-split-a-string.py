# use a counter to keep track of the number of each char
# as we add char to left (set), we decrement the counting variable
# when counter[char] == 0, we delete the key from counter
# if at any point len(left) == len(counter.keys()) we add 1 to out

from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        out = 0
        left = set()
        counter = Counter(s)
        
        for char in s:
            left.add(char)
            counter[char] -= 1
            if counter[char] == 0:
                counter.pop(char)
            if len(left) == len(counter.keys()):
                out+=1
        return out
    
    
        # # O(n^2) solution, thought it was too good to be true lol TLE'ed
        # for i in range(1, len(s)):
        #     left, right = s[:i], s[i:]
        #     # print(left, right)
        #     if len(set(left)) == len(set(right)):
        #         out+=1
        # return out