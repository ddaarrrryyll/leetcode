import bisect
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        arr1_count = Counter(arr1)
        for num in arr2:
            res.extend([num for i in range(arr1_count[num])])
        extra = []
        for num, count in arr1_count.items():
            if num not in arr2:
                while count > 0:
                    bisect.insort(extra, num)
                    count -= 1
        res.extend(extra)
        return res