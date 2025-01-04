class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        
        m = len(s)
        n = len(p)
        # i, j = 0, 0

        idx = p.find("*")
        prefix = p[:idx]
        suffix = p[idx+1:]

        # print(f"{prefix=} {suffix=}")

        i = s.find(prefix)
        j = s.rfind(suffix)

        # print(f"{i=} {j=}")

        if i + len(prefix) > j:
            return False

        if i >= 0 and j >= 0 and i < j:
            return True

        if prefix == ''  and i ==j:
            return True
            
        return False
        # while i < m and j < n:
        #     if p[j] == '*':

        #         if j+1 < n and p[j+1] == s[i]:
        #             return True
        #         j+=1
        #         i+=1
        #         continue
            
        #     if s[i] == p[j]:
        #         i+=1
        #         j+=1
        #     else:
        #         i+=1

        # if j<n :
        #     if p[j] == "*":
        #         return True
            
        #     return False

        # return True
        