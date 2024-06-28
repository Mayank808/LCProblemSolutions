# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height balanced implies that there is a abs different between every nodes 
        # height of left and right node of atmost 1 

        # Other Approaches:
        # Instead or returning h and valid, only return h and h == -1 if invalid
        def dfs(root):
            if not root:
                return 0, True

            h_left, l_valid = dfs(root.left)
            if not l_valid:
                return h_left, False

            h_right, r_valid = dfs(root.right) 

            return max(h_right, h_left) + 1,  l_valid and r_valid and abs(h_left - h_right) <= 1 

        h, valid = dfs(root)

        return valid
