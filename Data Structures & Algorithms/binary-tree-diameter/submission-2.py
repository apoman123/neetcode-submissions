# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_max_depth(self, node):
        if not node:
            return 0
        else:
            return max(self.find_max_depth(node.left), self.find_max_depth(node.right)) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        max_diameter = 0
        while stack:
            node = stack.pop()
            current_diameter = self.find_max_depth(node.left) + self.find_max_depth(node.right)

            if max_diameter < current_diameter:
                max_diameter = current_diameter
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return max_diameter
            