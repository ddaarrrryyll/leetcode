class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]): return mat;
        a = 0
        l = []
        ans = [[0 for _ in range(c)] for __ in range(r)]
        for m in range(len(mat)):
            for n in range(len(mat[0])):
                l.append(mat[m][n])
        
        for i in range(r):
            for j in range(c):
                print(f"{a=} {i=} {j=}")
                ans[i][j] = l[a]
                a += 1
        return ans