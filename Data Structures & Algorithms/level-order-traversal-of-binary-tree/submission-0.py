# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            queue = [root]
            result = []
            while queue:
                layer_nodes = []
                while queue:
                    layer_nodes.append(queue.pop(0))
                values = [node.val for node in layer_nodes]
                result.append(values)

                for node in layer_nodes:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)         
                    
            return result     

        else:
            return []



        