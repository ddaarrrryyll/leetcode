import java.util.stream.*;

class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = IntStream.of(nums).sum();
        System.out.println("each array must have sum: " + sum/k);
        if (k == 0 || sum % k != 0) return false;
        else return canPartition(0, nums, new boolean[nums.length], k, 0, sum/k);
    }
    
    public boolean canPartition(int start, int[] nums, boolean[] used, int k, int currSum, int targetSum) {
        // if one more bucket left means partitioning succeeded
        if (k==1) return true;
        // second base case
        if (currSum > targetSum) return false;
        
        // finished one bucket
        if (currSum == targetSum) return canPartition(0, nums, used, k-1, 0, targetSum);
        for (int i = start; i < nums.length; i++) {
            // if element is not used
            if (!used[i]) {
                // marked as used
                used[i] = true;
                // check if able to partition
                if (canPartition(i+1, nums, used, k, currSum + nums[i], targetSum)) return true;
                // if cannot partition, then we dont choose nums[i]
                used[i] = false;
            }
        }
        // if no returns return false
        return false;
    }
}
