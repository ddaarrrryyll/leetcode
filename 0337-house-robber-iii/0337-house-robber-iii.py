# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def rob_subtree(root):
            if not root:
                return (0, 0)
            left = rob_subtree(root.left)
            right = rob_subtree(root.right)

            rob_curr = root.val + left[1] + right[1]
            dont_rob_curr = max(left) + max(right)
            return rob_curr, dont_rob_curr
        return max(rob_subtree(root))