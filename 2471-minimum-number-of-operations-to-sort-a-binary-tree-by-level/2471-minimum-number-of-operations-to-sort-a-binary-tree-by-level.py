# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Perform a level-order traversal to gather nodes at each level
        levels = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # Count the number of swaps needed to sort each level
        swaps = 0
        for level in levels:
            target = sorted(level)
            for i in range(len(level)):
                if level[i] != target[i]:
                    swaps += 1
                    # Swap the two elements in the level
                    idx = level.index(target[i])
                    level[i], level[idx] = level[idx], level[i]
        return swaps
        