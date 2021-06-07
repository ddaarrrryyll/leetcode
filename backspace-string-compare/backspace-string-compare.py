class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def newString(arr: [], string: str) -> [str]:
            for char in string:
                if char != "#":
                    arr.append(char)
                elif arr:
                    arr.pop()
            return arr
        if newString([], S) == newString([], T):
            return True
        else:
            False