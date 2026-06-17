# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        self.val_list.append(node.val)
        if node.right:
            self.inorder(node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.val_list = []
        self.inorder(root)
        for i in range(len(self.val_list)-1):
            if self.val_list[i] >= self.val_list[i+1]:
                return False

        return True