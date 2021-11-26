class Solution {
    public int searchInsert(int[] nums, int target) {
        int head = 0;
        int tail = nums.length-1;
        int mid; 
        
        while (head <= tail) {
            mid = head + (tail-head)/2;
            if (nums[mid] == target) return mid;
            
            if (nums[mid] < target) head = mid+1;
            
            else if (nums[mid] > target) tail = mid-1;
        }
        return head;
    }
}