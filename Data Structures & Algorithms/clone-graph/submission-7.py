"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        old_to_new = {}

        def clone_node(node):
            if node == None:
                return node
            
            if node in old_to_new:
                return old_to_new[node]
            
            # create a clone of the node 

            copy = Node(node.val)
            old_to_new[node] = copy

            for nbr in node.neighbors:
                copy.neighbors.append(clone_node(nbr))
            
            return copy
        
        return clone_node(node)

        