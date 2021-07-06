# return minimum size of the set of integers you can remove such that at least half of arr is removed
from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        sol = 0
        size = len(arr)
        d = defaultdict(lambda: 0)
        for x in arr:
            d[x] += 1
        e = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        # print(e)
        for key, val in e.items():
            if size > len(arr)/2:
                size -= val
                sol += 1
            else:
                break
        return sol