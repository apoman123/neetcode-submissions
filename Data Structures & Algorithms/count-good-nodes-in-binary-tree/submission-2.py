# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_count = 0

        def dfs(node, values):
            
            if not values:
                print(node.val)
                self.good_count += 1
            elif node.val >= max(values):
                print(node.val)
                self.good_count += 1

            new_values = values + [node.val]

           
            if node.left:
                dfs(node.left, new_values)

            if node.right:
                dfs(node.right, new_values)

            return 



        dfs(root, [])
        return self.good_count