# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find_smallest_node_and_parent(node, parent):
            if not node.left:
                return node, parent
            elif node.left:
                return find_smallest_node_and_parent(node.left, node)

        def remove_smallest_node(node, parent):
            smallest_node, smallest_parent = find_smallest_node_and_parent(node, parent)
            if smallest_parent:
                if smallest_node.right:
                    temp = smallest_node.right
                    smallest_node.right = None
                    smallest_parent.left = temp
                    return node, smallest_node
                else:
                    smallest_parent.left = None
                    return node, smallest_node
            else: # remove root
                temp = smallest_node.right
                node = temp
                return node, smallest_node
            
        for _ in range(k):
            root, smallest_node = remove_smallest_node(root, None)
            print(smallest_node.val)

        return smallest_node.val

                
            

            