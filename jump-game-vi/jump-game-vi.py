# greedy algo, keeps the curr max score in deq and pop irrelevant tuples

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        deq = deque([])
        
        for i in range(len(nums)):
            # deq[0][0] keeps track of the current position + score you are at, with all possible positions and scores after that
            # if position to i take more than k steps, we drop the first tuple 
            while deq and deq[0][0] < i - k:
                deq.popleft()
            
            # curr = cumulative score to position i
            if deq:
                curr = deq[0][1] + nums[i]
            else:
                # this only happens once (first index)
                curr = nums[i]
            
            # keep track of the max score possible and the position for it
            while deq and deq[-1][1] <= curr:
                deq.pop()
                
            deq.append((i,curr))
            
        return deq[-1][1]
                