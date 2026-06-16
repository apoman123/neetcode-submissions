# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_max_depth(self, node):
            if node.left != None:
                left_depth = self.find_max_depth(node.left)
            else:
                left_depth = 0

            if node.right != None:
                right_depth = self.find_max_depth(node.right)
            else:
                right_depth = 0
            
            depth = 1 + max(right_depth, left_depth)
            return depth



    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root != None:
            return self.find_max_depth(root)
        else:
            return 0

        
        