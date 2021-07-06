# return minimum size of the set of integers you can remove such that at least half of arr is removed
from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # gives the frequency of each element
        w = sorted(list(Counter(arr).values()), reverse = True)
        sol, half = 0, 0
        for i in w:
            if half < len(arr)//2:
                half += i
                sol += 1
            else:
                break
        return sol
    
        