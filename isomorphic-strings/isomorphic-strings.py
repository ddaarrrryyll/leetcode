class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        visited = []
        ss = []
        for char in s:
            if char not in visited:
                visited.append(char)
            ss.append(visited.index(char))
        print(visited, ss)
        visited = []
        tt = []
        for char in t:
            if char not in visited:
                visited.append(char)
            tt.append(visited.index(char))
        print(visited, tt)
        if ss == tt:
            return True
        else:
            return False