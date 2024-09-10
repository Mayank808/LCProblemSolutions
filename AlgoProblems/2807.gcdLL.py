# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head

        while cur and cur.next:
            val_gcd = math.gcd(cur.val, cur.next.val)

            temp = cur.next
            cur.next = ListNode(val_gcd, temp)
            cur = temp

        return head 
