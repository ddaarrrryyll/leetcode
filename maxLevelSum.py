# problem 1161 Maximum Level Sum of Binary Tree
"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        result = root.val
        l = []
        q = deque()
        q.append(root)
        level = 1
        while len(q) > 0:
            count = len(q)
            summ = 0
            while (count > 0):
                temp = q.popleft()
                summ += temp.val
                if (temp.left):
                    q.append(temp.left)
                if (temp.right):
                    q.append(temp.right)
                count -= 1
            print(summ, level)
            l.append(summ)
            level += 1
        return l.index(max(l)) + 1