# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ret = []
        current = head
        n = 0
        while current:
            current = current.next
            n += 1
        
        index = 0
        per = max(1, n // k)
        extra_one = n % k if n // k > 0 else 0

        while index < k:
            if not head:
                ret.append(None)
                index += 1
                continue
            cur = head
            ret.append(cur)

            check = 0
            count = per - 1 + (1 if index < extra_one else 0)
            while head and count:
                head = head.next
                count -= 1
            
            if not head:
                continue 

            temp = head.next
            head.next = None
            head = temp

            index += 1

        return ret
