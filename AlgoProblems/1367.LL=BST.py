# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(pi, pattern_index, pattern, node):
            if pattern_index == len(pattern):
                return True
            
            if not node:
                return False
                
            while pattern_index > 0 and pattern[pattern_index] != node.val:
                pattern_index = pi[pattern_index - 1]
                
            if pattern[pattern_index] == node.val:
                pattern_index += 1
            
            return dfs(pi, pattern_index, pattern, node.left) or  dfs(pi, pattern_index, pattern, node.right)
                

        # KNP approach
        if not head and not root:
            return True
        if not head:
            return False
        
        pattern = [head.val]
        pi = [0]
        prefix = 0
        listnode = head.next

        while listnode:
            pattern.append(listnode.val)

            while prefix > 0 and pattern[prefix] != listnode.val:
                prefix = pi[prefix - 1]
            
            prefix += 1 if listnode.val == pattern[prefix] else 0
            pi.append(prefix)
            listnode = listnode.next


        return dfs(pi, 0, pattern, root)
            


        # Approach #1: O(mxn)
        # def checkSubPath(node, listnode):
        #     if not node:
        #         return False
    
        #     if dfs(node, listnode):
        #         return True
            
        #     return checkSubPath(node.left, listnode) or checkSubPath(node.right, listnode)
        
        # def dfs(node, head):
        #     if head is None:
        #         return True  # All nodes in the list matched
        #     if node is None:
        #         return False  # Reached end of tree without matching all nodes
        #     if node.val != head.val:
        #         return False  # Value mismatch
        #     return dfs(node.left, head.next) or dfs(node.right, head.next)

        # return checkSubPath(root, head)

                
