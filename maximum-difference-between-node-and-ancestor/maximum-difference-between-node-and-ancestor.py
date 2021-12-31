# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    max_diff = 0
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            children = [root.val]
            if root.left:
                children.extend(dfs(root.left))
            if root.right:
                children.extend(dfs(root.right))
                
            min_child, max_child = min(children), max(children)    
            # print(min_child, max_child)
            
            diff = max(abs(root.val - min_child), abs(root.val - max_child))
            
            self.max_diff = max(diff, self.max_diff)
            # print(self.max_diff)
            
            return min_child, max_child
        
        dfs(root)
        return self.max_diff
        
        