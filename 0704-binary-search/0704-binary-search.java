class Solution {
    public int search(int[] nums, int target) {
        int head = 0;
        int tail = nums.length-1;
        int mid;
        int mid_num;
        while (head <= tail) {
            mid = head + (tail - head) / 2;
            mid_num = nums[mid];
            if (mid_num == target) {
                return mid;
            } else if (mid_num < target) {
                head = mid+1;
            } else if (mid_num > target) {
                tail = mid-1;
            }
        }
        return -1;
    }
}