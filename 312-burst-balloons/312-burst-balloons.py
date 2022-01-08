class Solution(object):
    def maxCoins(self, nums):
        # similar to matrix multiplication | use dp
        
        # both ends are 1
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in nums]
        
        # narrowing the subarray to focus on (-3 because we just want to focus on the last x balloons in original array)
        for i in range(len(nums) - 3, -1, -1):
            # j is the balloon that is the limit we can burst to (ie we cannot burst past j)
            for j in range(i + 2, len(nums)):
                temp = []
                # k is the balloon that is getting burst
                for k in range(i+1, j):
                    # dp[i][k] and dp[k][j] is the current maximum for bursting balloons on either side of k
                    temp.append(dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
                
                dp[i][j] = max(temp)
                # for row in dp: print(row)
                # print("----------------------------")
        
        # maximum attainable coins is the last column of first row
        return dp[0][len(nums) - 1]