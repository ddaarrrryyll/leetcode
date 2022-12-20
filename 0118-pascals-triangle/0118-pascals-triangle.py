class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        i = 0
        while i < numRows:
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                row = [1,]
                for j in range(0, i-1):
                    n1, n2 = res[i-1][j:j+1+1]
                    row.append(n1 + n2)
                row.append(1)
                res.append(row)
            i += 1
        return res