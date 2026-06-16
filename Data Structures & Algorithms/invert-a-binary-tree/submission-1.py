# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inversion(self, node):
        if node.left != None:
            self.inversion(node.left)
        if node.right != None:
            self.inversion(node.right)
        
        tmp_node = None
        tmp_node = node.left 
        node.left = node.right
        node.right = tmp_node
        return node
        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root != None:
            return self.inversion(root)
        else:
            return None