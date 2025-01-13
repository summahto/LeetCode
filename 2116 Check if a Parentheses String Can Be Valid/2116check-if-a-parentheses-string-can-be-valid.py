class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s) 
        
        if n% 2 == 1:
            return False
        
        # for tracking indices of (
        stack = [] 
        # for tracking the indices of s than can be modified as per our needs
        openClosed = []

        for i in range(n):
            
            if locked[i] == '0':
                openClosed.append(i)
            else:
                # for every '(' insert a ')' which can be matched later on
                if s[i] == '(':
                    stack.append((')', i))
                
                elif s[i] == ')':
                    # check in stack first
                    if stack and stack[-1][0] == s[i]:
                        stack.pop()
                    # check in openClosed
                    elif openClosed and openClosed[-1] < i: 
                        openClosed.pop()
                    # if did not find a corresponding index for ')' => invalid
                    else:
                        return False
        
        # print(f"{stack=} {openClosed=}")

        while stack and openClosed:
            if stack[-1][1] < openClosed[-1]:
                stack.pop()
                openClosed.pop()
            else:
                break
        
        if stack :
            return False

        if len(openClosed) %2 ==1:
            return False
        
        return True
            