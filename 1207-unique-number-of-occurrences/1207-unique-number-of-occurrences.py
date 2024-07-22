class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        temp = [v for k, v in count.items()]
        return len(set(temp)) == len(temp)
            