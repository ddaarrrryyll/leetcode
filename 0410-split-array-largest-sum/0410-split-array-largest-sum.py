class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == len(nums): return max(nums)
        if k == 1: return sum(nums)
        
        # largest min sum is between max(nums) and sum(nums), we can do bin search
        lower, upper = max(nums), sum(nums)
        while lower < upper:
            mid = (lower + upper) // 2
            subarr_sum, subarr_count = 0, 1
            # if we find a way to partition nums into subarr_sum <= mid, we try to find a smaller mid, otherwise mid is too small and we need to increase
            for num in nums:
                if subarr_sum + num <= mid:
                    subarr_sum += num
                else:
                    subarr_sum = num
                    subarr_count += 1
                    
            # if we have more subarrays than k, then mid is too small
            if subarr_count > k:
                lower = mid + 1
            else:
                upper = mid
        return upper