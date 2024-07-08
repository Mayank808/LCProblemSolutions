# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=None)
        p1 = dummy
        carry = 0
        while l1 or l2:
            val = carry

            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            carry = val // 10
            val = val % 10

            p1.next = ListNode(val=val, next=None)
            p1 = p1.next
        
        if carry:
            p1.next = ListNode(val=carry, next=None)
        
        return dummy.next
