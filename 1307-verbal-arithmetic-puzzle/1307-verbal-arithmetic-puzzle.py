class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        allWords = words + [result]
        first_char = set()
        for word in allWords:
            if len(word) > 1:
                first_char.add(word[0])
        # get length of the longest word
        n = max(map(len, allWords))
        # if result is shorter than longest word we can stop
        if len(result) < n: return False
        
        def dfs(charIdx, wordIdx, carry, visited, c2d):
            # we are traversing top to bottom, right to left
            
            # if we reach the last char in the longest word carry should be 0 because it wont be last char otherwise
            if charIdx == n: return carry == 0
            # if we reach the final word; we are traversing from the right to left with -charIdx-1
            if wordIdx == len(allWords):
                # check final status for current digit
                sums = sum(c2d[word[-charIdx - 1]] if charIdx < len(word) else 0 for word in words) + carry
                
                if sums % 10 == c2d[result[-charIdx - 1]]:
                    # check next char (left of curr)
                    return dfs(charIdx + 1, 0, sums//10, visited, c2d)
                else:
                    return False
            
            # if current word length is too short we go to next word
            if wordIdx < len(words) and charIdx >= len(words[wordIdx]):
                return dfs(charIdx, wordIdx + 1, carry, visited, c2d)
            
            # current char
            c = allWords[wordIdx][-charIdx-1]
            # if char is mapped we can go to next word
            if c in c2d:
                return dfs(charIdx, wordIdx+1, carry, visited, c2d)
            else:
                # if c is the left most char, it must be 1
                firstDigit = 1 if c in first_char else 0
                for digit in range(firstDigit, 10):
                    if digit not in visited:
                        visited.add(digit)
                        c2d[c] = digit
                        if dfs(charIdx, wordIdx + 1, carry, visited, c2d.copy()): return True
                        # if wrong mapping, remove
                        else:
                            visited.remove(digit)
                return False
        
        return dfs(0, 0, 0, set(), {})