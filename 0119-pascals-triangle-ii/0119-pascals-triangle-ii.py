class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def nCr(n, r):
            return factorial(n) // factorial(r) // factorial(n-r)
        res = []
        for i in range(rowIndex+1):
            res.append(nCr(rowIndex, i))
        return res