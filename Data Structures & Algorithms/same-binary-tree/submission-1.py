# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        elif p != None and q != None:
            p_stack = []
            q_stack = []

            # initialize
            p_stack.append(p)
            q_stack.append(q)
            
            while len(p_stack) != 0 and len(q_stack) != 0:
                current_p = p_stack.pop()
                current_q = q_stack.pop()

                if current_p.val != current_q.val:
                    print("1")
                    return False
                else:
                    if current_p.left and current_q.left:
                        p_stack.append(current_p.left)
                        q_stack.append(current_q.left)
                    elif not current_p.left and  not current_q.left:
                        pass
                    else:
                        print("2")
                        return False
                    
                    if current_p.right and current_q.right:
                        p_stack.append(current_p.right)
                        q_stack.append(current_q.right)
                    elif not current_p.right and  not current_q.right:
                        pass
                    else:
                        print("3")
                        return False

            return True
        else:
            return False