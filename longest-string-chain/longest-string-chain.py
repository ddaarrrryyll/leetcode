# dp with dict? 2d array seems abit hard to implement

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        DP = {}
        # need to sort words first
        words.sort(key=len)
        print(words)
        for word in words:
            # keep track of size if shortest word starts with word
            DP[word] = 1
            
            # checking for different arrangements that can lead to this current word
            for i in range(len(word)):
                old = word[:i] + word[i+1:]
                if old in DP.keys():
                    # compare current value with all old (shorter) words
                    DP[word] = max(DP[old] + 1, DP[word])
        
        return max(DP.values())