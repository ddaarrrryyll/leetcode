class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        # first will always try to be the smallest
        # everytime there is a number bigger than the first, and not smaller than second, then we take it as second
        # otherwise if smaller than second it would be third
        
        first, second = float('inf'), float('inf')
        
        for num in nums:
            if second < num: return True
            if num <= first:
                first = num
            else:
                second = num
                
        return False