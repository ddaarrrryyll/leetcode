class Solution:
    def customSortString(self, order: str, str: str) -> str:
        ans = ""
        cnt = Counter(str)
        for c in order:
            if cnt[c] > 0:
                ans += cnt[c] * c
            del cnt[c]
        for c, v in cnt.items():
            ans += v * c
        return ans