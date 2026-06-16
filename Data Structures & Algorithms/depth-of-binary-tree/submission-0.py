# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def noChild(self, node):
        if node.left == None or node.right == None:
            return True
        else:
            return False
    
    def find_max_height(self, node):
        if node == None:
            return 0
        else:
            return max(self.find_max_height(node.left), self.find_max_height(node.right)) + 1 
        
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root != None:
            return self.find_max_height(root)
        else:
            return 0
        


