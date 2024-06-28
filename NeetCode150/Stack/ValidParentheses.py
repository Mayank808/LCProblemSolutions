class Solution:
    bracketType = {')' : '(', '}' : '{', ']' : '['}
    
    def isValid(self, s: str) -> bool:
        stack = []

        for par in s:
            if self.isOpeningBracket(par):
                stack.append(par)
                continue
            
            if not stack: 
                return False

            bracket = stack.pop()
            if self.bracketType[par] != bracket:
                return False
        
        if stack:
            return False

        return True
                
    
    def isOpeningBracket(self, c):
        return c in ('(', '{', '[')