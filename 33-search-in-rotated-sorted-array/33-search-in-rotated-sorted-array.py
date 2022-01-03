class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # find the index of the smallest element
        head, tail = 0, len(nums)-1
        while head < tail:
            mid = head + (tail-head)//2
            # if mid > tail, then start is on right half
            if nums[mid] > nums[tail]:
                head = mid+1
            # start is on left half
            else:
                tail = mid
        
        # find the partition of the array target lies in
        start = head
        head, tail = 0, len(nums)-1
        # if target > head and target >= start, then tail = start
        if target >= nums[start] and target <= nums[tail]:
            head = start
        else:
            tail = start
        
        # finding the actual position:
        while head <= tail:
            if target == nums[head]: return head
            if target == nums[tail]: return tail 
        
            mid = head + (tail-head)//2
            if target > nums[mid]:
                head = mid + 1
            elif target < nums[mid]:
                tail = mid - 1
            else:
                return mid
        return -1
            
        