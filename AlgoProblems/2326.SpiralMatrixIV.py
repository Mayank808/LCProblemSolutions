# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]

        cur = head
        row, col = 0, 0
        dir_row, dir_col = 0, 1

        # dirc_map = {
        #     (0, 1) : (-1, 0),
        #     (-1, 0) : (0, -1),
        #     (0, -1) : (1, 0),
        #     (1, 0) : (0, 1)
        # }

        start_row, end_row = 0, m
        start_col, end_col = -1, n

        while cur:
            # print(row, col, dir_row, dir_col)
            # print(res)
            res[row][col] = cur.val

            if dir_col == 1 and col + 1 >= end_col:
                # go down
                dir_row, dir_col = 1, 0
                end_col -= 1
            
            elif dir_col == -1 and col - 1 <= start_col:
                # go up
                dir_row, dir_col = -1, 0
                start_col += 1
            elif dir_row == 1 and row + 1 >= end_row:
                dir_row, dir_col = 0, -1
                end_row -= 1
            elif dir_row == -1 and row - 1 <= start_row:
                dir_row, dir_col = 0, 1
                start_row += 1
            
            row += dir_row
            col += dir_col

            cur = cur.next

        return res
