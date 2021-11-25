import java.lang.Math;

class Solution {
    public int maxSubArray(int[] nums) {
        int out = Integer.MIN_VALUE;
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            out = Math.max(out, sum);
            if (sum < 0) sum = 0;
        }
        return out;
    }
}