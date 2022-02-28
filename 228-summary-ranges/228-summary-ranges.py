class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        s = ""
        idx = 0
        
        while idx < len(nums):
            if idx == len(nums)-1 or nums[idx+1]-1 > nums[idx] or nums[idx+1] == nums[idx]:
                s += str(nums[idx])
                ans.append(s)
                s = ""
                idx += 1
                continue
                
            if not s:
                s = str(nums[idx])+"->"
            else:
                idx += 1
                continue
    
        return ans