class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        ans = 0
        
        # window size = win_len (x) , add to ans arithmetic sum of 1 to x-2
        # (win_len-2) * (win_len-1) // 2
        
        win_len = 0
        prev_change = float("inf")
        
        for i in range(1, len(nums)):
            change = nums[i]-nums[i-1]
            if change == prev_change:
                win_len += 1
                
            else:
                if win_len >= 3:
                    ans += (win_len-2) * (win_len-1) // 2
                
                # reset window length to represent [prev_num, curr_num]
                win_len = 2
                prev_change = change
                
        if win_len >= 3:
            ans += (win_len-2) * (win_len-1) // 2

        return ans