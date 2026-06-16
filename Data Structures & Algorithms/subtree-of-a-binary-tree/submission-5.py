# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def find_node(self, root, node):
        nodes = []
        queue = [root]
        while queue:
            current = queue.pop(0)

            if current.val == node.val:
                nodes.append(current)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return nodes

    def isSame(self, root1, root2):
        def update_queue(queue, node):
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            return queue
        queue1 = [root1]
        queue2 = [root2]
        while queue1 and queue2:
            root1 = queue1.pop(0)
            root2 = queue2.pop(0)

            if root1.val != root2.val:
                return False
            queue1 = update_queue(queue1, root1)
            queue2 = update_queue(queue2, root2)
        if len(queue1) != len(queue2):
            return False
        else:
            return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes = self.find_node(root, subRoot)
        for node in nodes:
            if self.isSame(node, subRoot):
                return True

        return False

        