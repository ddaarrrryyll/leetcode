class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        extra_gas, leftover, start = 0, 0, 0
        
        # at each iteration we check how much extra we have
        for i in range(len(gas)):
            extra_gas += gas[i] - cost[i]
            leftover += gas[i] - cost[i]
            
            # go to next iteration if we run out
            if leftover < 0:
                leftover = 0
                start = i + 1
        return -1 if (extra_gas < 0) else start
            