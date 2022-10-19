class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        counter_sorted = sorted(counter.items(), key = lambda pair: (-pair[1], pair[0]))
        return [counter_sorted[i][0] for i in range(k)]