# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # binary tree = recursive always
        """
        height of the left subtree and right subtree of any node does not differ by more than 1
        """
        return self.height(root) >= 0
        
    def height(self, root):
        if not root: return 0
        left_height, right_height = self.height(root.left), self.height(root.right)
        
        # if subtree differ more than 1
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        
        # return the height of this sub tree
        return max(left_height, right_height) + 1
            
        