# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = ListNode(next=head)
        res = left
        nright = head

        while n > 0 and nright:
            nright = nright.next
            n -= 1

        while nright:
            left = left.next
            nright = nright.next

        left.next = left.next.next

        return res.next
