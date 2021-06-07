class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()
            if (first - second) != 0:
                stones.append(first - second)
                stones.sort()
        return stones[0] if stones else 0
