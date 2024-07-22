class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        threshold = max_candy - extraCandies
        return [True if x >= threshold else False for x in candies]