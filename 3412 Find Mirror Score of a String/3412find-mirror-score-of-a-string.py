class Solution:
    def calculateScore(self, s: str) -> int:

        charMap = {}
        
        i,  j = 97, 122
        while i < j:
            charMap[chr(i)] = chr(j)
            charMap[chr(j)] = chr(i)
            i+=1
            j-=1

        # print(charMap)

        i, j = 0, 0
        ans = 0
        # dict of max Heap
        # ok, max heap makes sense, but why did you not think of stack?
        # Essentially, Question is aksing pick up the latest occurrence of the mirror element and then add the diff to the score
        # already have a map for mirrors
        # just store the indices of original element in LIFO manner 
        # so this should be a dict of stack

        unmarked = defaultdict(list)
        
        while i < len(s):
            if charMap[s[i]] in unmarked and unmarked[charMap[s[i]]] :
                # take out the latest occ and update the score 
                j = unmarked[charMap[s[i]]].pop()
                ans+= i- j
            else:
                unmarked[s[i]].append(i)
            
            i+=1

        return ans