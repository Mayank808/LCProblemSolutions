# most important thing to remember is to use tuple coordinates for the boxs. 
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '.': 
                    continue
            
                if (board[row][col] in rows[row] 
                or board[row][col] in cols[col] 
                or board[row][col] in boxs[(row // 3, col // 3)]):
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxs[(row // 3, col // 3)].add(board[row][col])
        
        return True
