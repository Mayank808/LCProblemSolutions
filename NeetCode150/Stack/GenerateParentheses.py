class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursive approach, two possibilites at each recursive step
        # 1. Append (. This can happen every iteration
        # 2. Append ). Can only happen if previous val is (
        
        res = []
        stack = ['(']
        def dfs(left, right):
            if (left + right) == 2 * n:
                res.append(''.join(stack))
                return
            
            if left < n:
                stack.append('(')
                dfs(left + 1, right)
                stack.pop()

            if right < left:
                stack.append(')')
                dfs(left, right + 1)
                stack.pop()
        
        dfs(1, 0)

        return res

