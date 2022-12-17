class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        prev = ''
        out = []
        for word in words:
            word_check = ''.join(sorted(list(word)))
            if word_check == prev:
                continue
            else:
                prev = word_check
                out.append(word)
        return out