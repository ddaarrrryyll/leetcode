class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        # TLE soln
        
        curr_sum = 0
        # base case, numbers is empty
        if not nums:
            return curr_sum

        # if numbers is not empty
        else:
            n = len(nums)
            # if length of numbers >= 2
            if n > 2:
                first = nums[0] # 4
                second = nums[1] # 6
                choose_first = self.rob(nums[2:n])
                choose_second = self.rob(nums[3:n])

                # choose the value with the bigger sublist
                if first + choose_first > second + choose_second:
                    curr_sum += (first + choose_first)

                elif first + choose_first < second + choose_second:
                    curr_sum += (second + choose_second)

                else:
                    curr_sum += (first + choose_first)

            # if only two or less number left in list
            else:
                return max(nums)


        # otherwise return obtained sum
        """
        @lru_cache
        def dfs(i):
            if i < len(nums):
                # choose between dont take and take + skip
                return max(dfs(i+1), nums[i] + dfs(i+2))
            else:
                return 0
            
        return dfs(0)