# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        
        new = PolyNode()
        start = new
        p1, p2 = poly1, poly2

        while p1 or p2:
            if not p2:
                start.next = PolyNode(p1.coefficient, p1.power)
                p1 = p1.next
            elif not p1:
                start.next = PolyNode(p2.coefficient, p2.power)
                p2 = p2.next
            elif p1.power == p2.power:
                if p1.coefficient + p2.coefficient:
                    start.next = PolyNode(p1.coefficient + p2.coefficient, p1.power)
                p1 = p1.next
                p2 = p2.next
                if not start.next:
                    continue
            elif p1.power > p2.power:
                start.next = PolyNode(p1.coefficient, p1.power)
                p1 = p1.next
            else:
                start.next = PolyNode(p2.coefficient, p2.power)
                p2 = p2.next

            start = start.next



        return new.next
