class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def isValid(s) :
            chars = set()

            for ch in s:
                if ch in chars :
                    return False
                else :
                    chars.add(ch)

            return True
        
        def dp(start, curr, uniq):
            
            uniq.add(curr)
            # outer.add(uniq)

            for i in range(start, len(arr)):
                
                if not isValid(arr[i]):
                    continue

                if len(set(curr) & set(arr[i])) != 0:
                    continue

                curr += arr[i]
                dp(i+1, curr, uniq)
                curr = curr[0: len(curr) - len(arr[i])]

        res = set()
        dp(0, "", res)
        # print(res)

        return max(len(s) for s in res)