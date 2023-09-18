class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            count = mat[i].count(1)
            bisect.insort(res, (count, i))
        return [tup[1] for tup in res[0:k]]