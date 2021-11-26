class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        
        @cache
        def dp(stone, jump):
            # destination stone after jump
            dest = stones[stone] + jump
            
            # if reached end
            if dest == stones[n-1]:
                return True
            
            # find destination stone in list
            pos = bisect.bisect_left(stones, dest, stone+1, n)
            # print(f"{stones[stone] = } jump to {stones[pos] = }, {jump = }")
            # if cannot find; pos == n means dest further than last stone, stones[pos] > dest means distance jumped could not reach stone 
            if pos == n or stones[pos] > dest:
                # print('break')
                return False
            
            # no 0 jumps
            jumps = [jump-1, jump, jump+1] if jump!=1 else [jump, jump+1]
            return any(dp(pos, jump) for jump in jumps)
            
        return dp(0, 1)