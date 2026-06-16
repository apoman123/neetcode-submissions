# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, node):
        result = []
        if node.left:
            result = result + self.inorder(node.left)
        result.append(node.val)
        if node.right:
            result = result + self.inorder(node.right)
        return result

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = self.inorder(root)
        return result[k-1]
        