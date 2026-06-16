# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_len(head):
            current_node = head
            count = 0
            while current_node:
                current_node = current_node.next
                count += 1
            return count
        
        def get_nth_node(head, n):
            count = 0
            current_node = head
            prev = None
            while count != n and current_node:
                count += 1
                prev = current_node
                current_node = current_node.next
            return current_node, prev

        total_len = get_len(head)
        nth = total_len - n 
        node, prev = get_nth_node(head, nth)
        if prev:
            prev.next = node.next
            node.next = None
        else:
            head = node.next
            node.next = None
        return head


        

        