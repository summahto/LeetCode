class Solution:
    def isValid(self, s: str) -> bool:

        if s[0] == ']' or s[0] == '}' or s[0] == ')':
            return False

        n =len(s)
        paraMap = dict()
        
        paraMap['('] = ')'
        paraMap['{'] = '}'
        paraMap['['] = ']'

        stack = []
        i = 0
        while i < n:
            
            if s[i] in paraMap:
                stack.append(paraMap[s[i]])

            elif stack and stack[-1] == s[i]:
                stack.pop()

            elif stack and stack[-1] != s[i]:
                return False

            elif s[i] not in paraMap:
                return False

            i+=1
        
        if stack:
            return False
        
        return True