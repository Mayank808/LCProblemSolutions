# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recurse down left and right path dfs
        # return true if you have found either p or q 
        # all values are unique so if left and right return true we have reached a valid decendant

        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur

        # # Approach #1: Recursive
        # def dfs(node):
        #     if not node:
        #         return
    
        #     if p.val < node.val and q.val < node.val:
        #         return dfs(node.left)
        #     elif p.val > node.val and q.val > node.val:
        #         return dfs(node.right)
        #     else:
        #         return node
        
        # return dfs(root)
            
