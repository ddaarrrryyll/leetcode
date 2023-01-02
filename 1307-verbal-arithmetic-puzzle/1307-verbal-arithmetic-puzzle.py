class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # combine all the words into one array
        allWords = words + [result]
        # collect all the first characters of the words (this is to make sure it starts at 1 when we iterate possibilities)
        firstChar = set([word[0] for word in allWords if len(word) > 1])
        # early checking
        # get the length of the longest word, if result is shorter than it we can return
        n = max(map(len, allWords))
        if len(result) < n: return False
        
        # we traverse top to bottom, for right to left col
        def backtrack(charIdx, wordIdx, carry, visited, c2d):
            # we use word[-charIdx-1] to access each char right to left
            # basecase: reaching first char of longest word
            if charIdx == n: return carry == 0
            
            # if we finished processing
            if wordIdx == len(allWords):
                sums = 0
                # sum up all the chars in that word
                for word in words:
                    if charIdx < len(word):
                        sums += c2d[word[-charIdx-1]]
                sums += carry
                # if this sum % 10 does not give result[-charIdx-1], it is wrong
                if sums % 10 != c2d[result[-charIdx-1]]:
                    return False
                else:
                    return backtrack(charIdx+1, 0, sums//10, visited, c2d)
            # to check if we have more chars to add
            if wordIdx < len(words) and charIdx >= len(words[wordIdx]):
                return backtrack(charIdx, wordIdx+1, carry, visited, c2d)
                
            # mapping of chars
            c = allWords[wordIdx][-charIdx-1]
            if c in c2d:
                return backtrack(charIdx, wordIdx+1, carry, visited, c2d)
            else:
                start = 0 
                if c in firstChar:
                    start = 1
                for digit in range(start, 10):
                    if digit not in visited:
                        visited.add(digit)
                        c2d[c] = digit
                        if backtrack(charIdx, wordIdx+1, carry, visited, c2d.copy()): return True
                        else:
                            visited.remove(digit)
                return False
            
        
        return backtrack(0, 0, 0, set(), {})
        
        