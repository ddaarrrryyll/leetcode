class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        # keep track of numbers of divisors
        DP = [1 for _ in nums]
        parent = [0 for _ in nums]
        
        maxLen = 0
        maxIdx = 0
        
        # traverse nums array
        for i in range(len(nums)):
            parent[i] = i
            
            # for numbers smaller than j
            for j in range(i):
                # if it's divisible, can add 1 to i's number of divisor, if is less than j's number of divisor, update
                if nums[i] % nums[j] == 0 and DP[i] < DP[j] + 1:
                    DP[i] = DP[j] + 1
                    # parent[i] is the biggest factor of i other than i itself
                    parent[i] = j
            
            # if size of maxLen number of factors of i, update maxLen
            if maxLen < DP[i]:
                maxLen = DP[i]
                maxIdx = i
            
        # array to be returned
        out = []
        k = maxIdx
        
        # traversing factors
        while (k != parent[k]):
            out.append(nums[k])
            k = parent[k]
        
        out.append(nums[k])
        
        return out