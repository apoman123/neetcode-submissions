# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def get_len(node):
            current_node = node
            count = 0
            while current_node:
                count += 1
                current_node = current_node.next
            return count
        
        def get_node_with_len(node, length):
            current_node = node
            length -= 1
            while current_node and length:
                current_node = current_node.next
                length -= 1
            return current_node
        
        def reverse_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        def remove_front_node(head):
            new_head = head.next
            head.next = None
            return new_head, head
            
 

        # def find_last(node):
        #     current_node = node
        #     while current_node.next:
                
        # find middle and cut in half
        length = get_len(head)
        middle_node = get_node_with_len(head, length // 2) if length % 2 == 0 else get_node_with_len(head, length // 2 + 1)
        back_list = middle_node.next
        middle_node.next = None
        back_list = reverse_list(back_list)
        front_list = head 
        nodes = []
        while front_list:
            front_list, front_node = remove_front_node(front_list)
            nodes.append(front_node)

            if back_list:
                back_list, back_node = remove_front_node(back_list)
                nodes.append(back_node)
        
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        
  

        
                
        
        
        

        