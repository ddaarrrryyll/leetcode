/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        // a height balanced tree has onnly a max depth diff of 1 between subtrees
        return height(root) >= 0;
    }
    
    public int height(TreeNode root) {
        if (root == null) return 0;
        int left_height = height(root.left);
        int right_height = height(root.right);
        
        if (left_height < 0 || right_height < 0 || Math.abs(left_height - right_height) > 1) return -1;
        
        return Math.max(left_height, right_height)+1;
    }
}