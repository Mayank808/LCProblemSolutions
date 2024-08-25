# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Idea #1 level order traversal and take right most value in array
        # Idea #2 dfs right first always and maintain recursive depth
        #   have a set that can be checked if we have seen that level before and 
        #   if not append value to array
        if not root: return []

        ret = []
        q = deque([root])

        while q:
            rightMostNode = None
            levelLen = len(q)

            for x in range(levelLen):
                node = q.popleft()

                if node:
                    rightMostNode = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightMostNode:
                ret.append(rightMostNode.val)
        
        return ret
            


