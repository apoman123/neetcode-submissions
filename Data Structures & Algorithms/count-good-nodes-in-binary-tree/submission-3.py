# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.buffer = []
        self.good_count = 0

        def check_path():
            if len(self.buffer) > 1:
                for i in range(len(self.buffer)-1):
                    if self.buffer[i].val > self.buffer[-1].val:
                        return False
            return True

        def dfs(node):
            self.buffer.append(node)
            if check_path():
                self.good_count += 1
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            self.buffer.pop()

        dfs(root)
        return self.good_count

