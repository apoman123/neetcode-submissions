# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            result = []
            queue = [root]
            while queue:
                nodes = []
                while queue:
                    nodes.append(queue.pop(0))
                result.append(nodes[-1].val)
                for node in nodes:
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)
                        
            return result
        else:
            return []