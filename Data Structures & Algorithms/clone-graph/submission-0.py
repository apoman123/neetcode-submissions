"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node):
            if not node.val in self.new_nodes:
                new_node = Node(node.val, None)
                self.new_nodes[node.val] = new_node
                neighbors = []
                if node.neighbors:
                    for neighbor in node.neighbors:
                        neighbors.append(dfs(neighbor))
                new_node.neighbors = neighbors
                return new_node
            else:
                return self.new_nodes[node.val]

        if node:
            self.new_nodes = {}
            return dfs(node)
        else:
            return None

        


    
        
