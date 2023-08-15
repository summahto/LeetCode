class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if(len(tokens) == 1):
            return int(tokens[0])
        
        stack = [] * len(tokens)
        i,j, ans = 0, 0, 0
        

        while i < len(tokens) :
            
            
            while((len(stack) != 0) and ((stack[-1] == '+') or (stack[-1] == '-') or (stack[-1] == '*') or (stack[-1] == '/'))): 

                if j == 0 :
                    op = stack.pop()
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                    exp = f"{operand2} {op} {operand1} "
                    # print("expression", exp)
                    ans = int(eval(exp))
                    # print("answer1", ans)
                    j += 1
                

                    
                else :
                    op = stack.pop()
                    operand = stack.pop()
                    exp = f"{operand} {op} {ans}"
                    # print("expression", exp)
                    
                    ans = int(eval(exp))
                    # print("answer2", ans)


            
            stack.append(tokens[i])
            # print("i", i)
            i += 1
        
        op = stack.pop()
        operand = stack.pop()
        exp = f"{operand} {op} {ans}"
                    
        ans = int(eval(exp))

        return ans


