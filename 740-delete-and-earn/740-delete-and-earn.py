class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        ans = 0
        
        for key in ctr.keys():
            ctr[key] = ctr[key] * key
            
        print(ctr)
        max_num = max(ctr.keys())
        DP = [0] * (max_num + 1)
        
        # points if we remove 1 from nums, default is 0 if there is no 1 in nums
        DP[1] = ctr[1]
        
        # for the rest of the numbers, we choose between the larger of the two:
        # 1) Removing the number, and we can add the sum of the number that is not adjacent
        # 2) Don't remove the number, and take the sum of the previous number
        
        for i in range(2, len(DP)):
            DP[i] = max(DP[i-1], DP[i-2] + ctr[i])
            
        return DP[max_num]
        