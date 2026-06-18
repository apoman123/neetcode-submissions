# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            p = None
            h = head
            a = head.next
            while h:
                h.next = p
                p = h
                h = a
                if a:
                    a = a.next
                
            return p
        else:
            return None


