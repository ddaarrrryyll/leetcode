class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counter = sorted([(v, k) for k, v in counter.items()], reverse=True)
        return [sorted_counter[i][1] for i in range(k)]