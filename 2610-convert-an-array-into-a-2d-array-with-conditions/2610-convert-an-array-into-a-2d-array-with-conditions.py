class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        rows = defaultdict(lambda: -1)
        count = Counter(nums)
        res = [[] for _ in range(max(count.values()))]
        for num in nums:
            res[rows[num]+1].append(num)
            rows[num] += 1
        return res