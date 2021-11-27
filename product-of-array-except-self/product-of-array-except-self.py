class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return
        
        i, temp = 1, 1
        res = [1 for i in range(n)]
        
        # setting res[i] to multiple of every element infront of it
        for i in range(n):
            res[i] = temp
            temp *= nums[i]
            
        temp = 1
        
        # multiplying res[i] to every element behind it
        for i in range(n - 1, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        return res
    
# prefix sum soultion
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # running product of prefix (front to back)
        p = list(accumulate(nums, mul))
        # running product of suffix (back to front, but flipped back after)
        s = list(accumulate(nums[::-1], mul))[::-1]
        # print(p)
        # print(s)
        
        out = []
        for i in range(len(nums)):
            if i > 0:
                pre = p[i-1]
            # if i is first element, prefix should be 1
            else:
                pre = 1
            
            if i+1 < len(nums):
                suf = s[i+1]
            # if i is last element, suffix should be 1
            else:
                suf = 1
                
            out.append(pre*suf)
            
        return out
