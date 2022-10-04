# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    
        # dfs
        
        if not root: return False
        
        if targetSum - root.val == 0 and not (root.right or root.left): return True
        
        found = False
        
        if root.left and not found: 
            found = self.hasPathSum(root.left, targetSum - root.val)
        if root.right and not found: 
            found = self.hasPathSum(root.right, targetSum - root.val)
        
        return found