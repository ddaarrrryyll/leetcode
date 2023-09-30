class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        mon_stack = deque()
        max_C = float("-inf")
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num < max_C:
                return True
            while mon_stack and num > mon_stack[0]:
                max_C = mon_stack.popleft()
                
            mon_stack.appendleft(num)
        return False