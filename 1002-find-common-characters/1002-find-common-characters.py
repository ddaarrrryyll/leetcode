class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        out = Counter(words[0])
        for word in words:
            out &= Counter(word)
        return list(out.elements())