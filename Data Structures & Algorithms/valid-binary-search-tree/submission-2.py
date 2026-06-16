# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs to do inorder traversal
        self.inorder = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            self.inorder.append(node.val)
            if node.right:
                dfs(node.right)
            return
        dfs(root)
        for i in range(len(self.inorder)-1):
            if self.inorder[i] >= self.inorder[i+1]:
                return False
        
        return True
