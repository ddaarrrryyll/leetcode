"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # base case
        if not root: return None
        
        # if given a node, store (level, node)
        dq = deque([(1, root)])
        # either parent or node on the left side
        pop_level = 0
        pop_node = None
        
        while dq:
            level, node = dq.popleft()
            # current node has the same level as the node that got popped
            if level == pop_level:
                pop_node.next = node
                pop_node = node
            else:
                pop_level, pop_node = level, node
                
            # adding children to dq
            if node.left:
                dq.append((level+1, node.left))
                dq.append((level+1, node.right))
                
        return root