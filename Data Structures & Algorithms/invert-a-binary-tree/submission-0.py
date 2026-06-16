# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # DFS
            node_stack = []
        
            # initialize 
            node_stack.append(root)

            while len(node_stack) != 0:
                current_node = node_stack.pop()
                
                # add childs to node_stack
                if current_node.left != None:
                    node_stack.append(current_node.left)
                if current_node.right != None:
                    node_stack.append(current_node.right)

                # exchange childs
                temp_node = current_node.left
                current_node.left = current_node.right
                current_node.right = temp_node
            return root
        else:
            return root
