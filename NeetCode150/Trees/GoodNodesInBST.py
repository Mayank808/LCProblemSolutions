# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs with cur_max passed each recursive call 
        if not root:
            return 0
        
        def dfs(node, cur_max):
            if not node:
                return 0
            
            val = 0
            if cur_max <= node.val:
                val = 1
                cur_max = node.val
                
            return val + dfs(node.left, cur_max) + dfs(node.right, cur_max)

        return dfs(root, root.val)
