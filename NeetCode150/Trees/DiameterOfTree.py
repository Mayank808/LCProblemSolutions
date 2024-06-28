# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # return max of left plus right and path

        def dfs(root):
            if not root:
                return 0, 0
            
            diam_left, h_left = dfs(root.left)
            diam_right, h_right = dfs(root.right)

            return max(diam_left, diam_right, h_left + h_right), max(h_left, h_right) + 1
        
        max_diam, h = dfs(root)

        return max_diam
