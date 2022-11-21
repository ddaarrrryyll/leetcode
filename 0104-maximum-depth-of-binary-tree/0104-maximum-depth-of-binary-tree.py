# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        out = 0
        if not root: return out
        out += 1
        out = max(self.maxDepth(root.left) + 1, out)
        out = max(self.maxDepth(root.right) + 1, out)
        return out