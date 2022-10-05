# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int, sub = None) -> Optional[TreeNode]:
        
        
        if depth == 1:
            return TreeNode(val, None, root) if sub == 'right' else TreeNode(val, root, None)
        
        if root.left or depth == 2:
            root.left = self.addOneRow(root.left, val, depth - 1, 'left')
        if root.right or depth == 2:
            root.right = self.addOneRow(root.right, val, depth - 1, 'right')
            
        return root