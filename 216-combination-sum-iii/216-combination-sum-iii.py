
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.util([], 1, k, n)
        return self.ans
    
    def util(self, path: list, head: int, k: int, n: int) -> None:
        flag = False
        if k == 0 and n == 0:
            flag = True
            self.ans.append(path)
        if k == 0 or n == 0:
            return
        for i in range(head, 10):
            if flag == True: break
            self.util(path+[i], i + 1, k - 1, n-i)