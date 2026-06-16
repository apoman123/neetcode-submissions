# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def find_nodes(self, root, target):
        stack = [root]
        nodes = []
        while stack:
            node = stack.pop()
            if node.val == target.val:
                nodes.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return nodes

    def same_tree(self, root1, root2):
        if (root1 and not root2) or (not root1 and root2):
            return False
        elif (not root1) and (not root2):
            return True
        else:
            stack1 = [root1]
            stack2 = [root2]
            while stack1 and stack2:
                node1 = stack1.pop()
                node2 = stack2.pop()
                if node1.val != node2.val:  
                    return False
                else:
                    if node1.left:
                        stack1.append(node1.left)
                    if node1.right:
                        stack1.append(node1.right)
                    if node2.left:
                        stack2.append(node2.left)
                    if node2.right:
                        stack2.append(node2.right)
                    
            if len(stack1) != len(stack2):
                return False
            else:
                return True


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes = self.find_nodes(root, subRoot)
        if nodes:
            for node in nodes:
                if self.same_tree(node, subRoot):
                    return True
            return False
        else:
            return False
