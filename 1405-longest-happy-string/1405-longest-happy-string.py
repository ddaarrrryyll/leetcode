class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0: heappush(heap, (-a, 'a'))
        if b > 0: heappush(heap, (-b, 'b'))
        if c > 0: heappush(heap, (-c, 'c'))
        
        # tup should hold (consec, budget, char)
        tup = None
        ans = []
        
        # try to use the char that has the highest budget first
        
        while len(heap) > 0:
            # budget, char for budget
            count, char = heappop(heap)
            count = -count
            # adding char to list will use one count
            ans.append(char)
            count -= 1
            
            # if we have already used up the limit (2), push count and char back to the heap
            if tup and tup[0] == 2:
                heappush(heap, (tup[1], tup[2]))
                tup = None
                
            # if there is still budget available and our consec has not been used up
            if count > 0:
                # if we have previously used the same char
                if tup and tup[2] == char:
                    tup = (tup[0] + 1, -count, char)
                else:
                    tup = (1, -count, char)
                    heappush(heap, (-count, char))
            
        return "".join(ans)