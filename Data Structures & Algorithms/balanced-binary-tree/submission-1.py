# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def find_max_height(self, node):
        if not node:
            return 0
        else:
            return max(self.find_max_height(node.left), self.find_max_height(node.right)) + 1
            

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return  True
        else:
            stack = [root]
            while stack:
                node = stack.pop()
                if node.left and node.right:
                    if (
                        (self.find_max_height(node.left) - self.find_max_height(node.right) > 1)
                        or
                        (self.find_max_height(node.left) - self.find_max_height(node.right) < -1)
                        ):
                        return False
                elif node.left and not node.right:
                    if self.find_max_height(node.left) > 1:
                        return False
                elif not node.left and node.right:
                    if self.find_max_height(node.right) > 1:
                        return False


                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            return True