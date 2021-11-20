class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return
        
        # every occurence of duplicate numbers will appear on even indices before the non duplciat number
        # every occurence of duplicate numbers will appear on odd indices after the non duplicate number
        head = 0
        tail = len(nums) - 1
        
        while head < tail:
            mid = head + (tail-head) // 2
            # print(f"{nums[head]=} {nums[tail]=} {nums[mid]=}")
            if nums[mid-1] == nums[mid]:
                if mid % 2 == 1:
                    head = mid + 1
                else:
                    tail = mid - 1 - 1
                    
            elif nums[mid+1] == nums[mid]:
                if mid % 2 == 1:
                    tail = mid - 1
                else:
                    head = mid + 1 + 1
            else:
                return nums[mid]
        else:
            return nums[head]