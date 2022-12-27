class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # create a hashmap of i, remaining pairs
        remaining = {}
        for i in range(len(capacity)):
            remaining[i] = capacity[i] - rocks[i]
        tup = [(k, v) for k, v in remaining.items()]
        tup = sorted(tup, key=lambda pair: pair[1])
        ans = 0
        for pair in tup:
            if pair[1] == 0:
                ans += 1
            else:
                if additionalRocks >= pair[1]:
                    ans += 1
                    additionalRocks -= pair[1]
                else:
                    return ans
        return ans