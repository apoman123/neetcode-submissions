# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_len(node):
            count = 0
            current = node
            while current:
                count += 1
                current = current.next
            return count
        
        def return_long_short(l1, l2):
            l1_len = get_len(l1)
            l2_len = get_len(l2)
            if l1_len >= l2_len:
                return l1, l2
            else:
                return l2, l1

        def get_last(node):
            current = node
            while current.next:
                current = current.next
            return current

        def get_right_value(value):
            if value >= 10:
                value = value % 10
                return value, 1
            else:
                return value, 0

        long, short = return_long_short(l1, l2)

        carry = 0
        current_long = long
        current_short = short
        while current_long:
            if current_short:
                new_value = current_long.val + current_short.val + carry
                new_value, new_carry = get_right_value(new_value)
                current_long.val = new_value
                carry = new_carry
                current_long = current_long.next
                current_short = current_short.next
            else:
                new_value, new_carry = get_right_value(current_long.val + carry)
                current_long.val = new_value
                carry = new_carry
                current_long = current_long.next

        if carry:
            get_last(long).next = ListNode(1, None)
        return long

        

