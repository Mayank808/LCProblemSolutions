class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Ideas
        # two seperate b search one on rows on cols
        # do b search like its a 1d array and take mods to get row and cols

        # Approach 2: Treat like a 1d array
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (right - left) // 2 + left

            row, col = divmod(mid, cols)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

        # # Approach 1: 2 bsearch on row and col
        # rows, cols = len(matrix), len(matrix[0])
        # top, bottom = 0, rows - 1

        # while top <= bottom:
        #     mid = (bottom - top) // 2 + top

        #     if matrix[mid][-1] < target:
        #         top = mid + 1
        #     elif matrix[mid][0] > target:
        #         bottom = mid - 1
        #     else:
        #         break
        # else:
        #     return False
        
        # row = (bottom - top) // 2 + top
        # left, right = 0, cols - 1

        # while left <= right:
        #     mid = (right - left) // 2 + left

        #     if matrix[row][mid] == target:
        #         return True
        #     elif matrix[row][mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return False
        
