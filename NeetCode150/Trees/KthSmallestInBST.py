# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:  
        # Approach #2: Iterative Stack Approach  
        n = 0
        stack = []
        cur = root

        while cur or stack:
            # recurse to left most position to get next smallest number
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()

            n += 1

            if n == k:
                return node.val
            
            # first recurse through direclty larger values from current smallest number
            cur = node.right
        
        return -1

        # Approach #1: build inOrderTraversal array and then return k from that array
        # ret = []
        
        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     ret.append(node.val)
        #     dfs(node.right)

        # dfs(root)
        # return ret[k - 1]
