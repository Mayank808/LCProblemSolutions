# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if not root:
            return []
        queue = deque([root])

        while queue:
            curLevelLen = len(queue)
            level = []

            for x in range(curLevelLen):
                node = queue.popleft()

                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if level:
                ret.append(level)
        
        return ret
      
        # Approach 2: Recursive DFS 
        # dfs, go left first then right while incrementing recursion depth each level traversal
        # append into respective height ret array

        # def dfs(node, depth):
        #     if not node:
        #         return 
        
        #     if len(ret) <= depth:
        #         ret.append([node.val])
        #     else:
        #         ret[depth].append(node.val)
            
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)


        # dfs(root, 0)
        # return ret


