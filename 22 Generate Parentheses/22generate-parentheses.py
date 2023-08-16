class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        list = []
        self.paraGen('', 0, 0, n, list)
        return list

        
        
    def paraGen(self, s, open, close, max, list):

        if len(s) ==  (max*2) :
            list.append(s)
            return
        
        if(open < max) :
            self.paraGen(s + "(", open + 1, close, max, list)
        
        if(close < open) :
            self.paraGen(s + ")", open, close + 1, max, list)
            
            

            
