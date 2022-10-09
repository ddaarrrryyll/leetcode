# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.helper(root, root, k)
    
    def bin_search(self, node, root, k) -> bool:
        curr = root
        while curr:
            if curr.val == k: return curr != node # eg k = 10, node = 5, root = 5 (same node)
            elif curr.val < k:
                curr = curr.right
            elif curr.val > k:
                curr = curr.left
        return False
    
    def helper(self, node, root, k) -> bool:
        if not node: return False
        if self.bin_search(node, root, k - node.val): return True
        return self.helper(node.left, root, k) or self.helper(node.right, root, k)