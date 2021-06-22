class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1
        
        # BS for smallest
        head = 0
        tail = len(nums) - 1
        
        while (head < tail):
            mid = head + (tail - head) // 2
            if (nums[mid] > nums[tail]):
                head = mid + 1
            else:
                tail = mid
            # print(f"head {head} tail {tail} mid {mid}")
        # print(nums[head])
        
        start = head
        head = 0
        tail = len(nums) - 1
        
        if (target >= nums[start] and target <= nums[tail]):
            head = start
        else:
            tail = start
        
        
        # BS for target   
        while head <= tail:
            
            if target == nums[head]:
                return head
            elif target == nums[tail]:
                return tail
            
            mid = head + (tail - head) // 2
            print(f"head {nums[head]} tail {nums[tail]} mid {nums[mid]}")            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                head = mid + 1
            else:
                tail = mid - 1
                
        return -1