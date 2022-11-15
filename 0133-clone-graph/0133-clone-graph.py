"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        to_visit = deque([node])
        clones = {
            node.val: Node(node.val, [])
        }
        while to_visit:
            curr = to_visit.popleft()
            curr_clone = clones[curr.val]
            
            for neighbour in curr.neighbors:
                if neighbour.val not in clones:
                    clones[neighbour.val] = Node(neighbour.val, [])
                    to_visit.append(neighbour)
                curr_clone.neighbors.append(clones[neighbour.val])
        return clones[node.val]