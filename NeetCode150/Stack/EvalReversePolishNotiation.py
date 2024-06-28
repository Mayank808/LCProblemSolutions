class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # traverse left to right
        # push value onto stack
        # if operand then pop two values off stack and use eval 
        # below code assumes valid expression
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '-':
                rval, lval = stack.pop(), stack.pop()
                stack.append(lval - rval)
            elif token == '/':
                rval, lval = stack.pop(), stack.pop()
                stack.append(int(lval / rval))
            else:
                stack.append(int(token))
        
        return stack[-1]

        # # Clean written solution: Eval is very slow however
        # stack = []
        # for token in tokens:
        #     if token in ('+', '-', '*', '/'): 
        #         rval, lval = stack.pop(), stack.pop()
        #         res = eval(f'{lval} {token} {rval}')
        #         stack.append(int(res))
        #         continue
            
        #     stack.append(int(token))
        
        # return stack[0]