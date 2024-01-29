class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        
        @lru_cache
        def helper(idx, mod):
            if idx == n:
                return 0 if mod == 0 else -inf
            if (idx, mod) in dp:
                return dp[(idx, mod)]
            j = helper(idx + 1, (mod + nums[idx]) % 3) + nums[idx]
            k = helper(idx + 1, mod)
            res = max(j, k)
            dp[(idx, mod)] = res
            return res
        
        return helper(0, 0)
    # https://www.youtube.com/watch?v=u_2kOwmJQW4