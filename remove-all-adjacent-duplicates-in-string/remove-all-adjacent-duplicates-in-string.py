class Solution:
    def removeDuplicates(self, s: str) -> str:
        check = []
        for c in s:
            # print(f"c = {c}")
            if not check or check[-1] != c:
                check.append(c)
            else:
                check.pop()
            # print(check)
        return "".join(check)