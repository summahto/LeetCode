class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        total = 0
        i, j = 0, 0
        min_cost = 0
        while i < len(s):

            start = ord(s[i]) - ord('a') 
            end = ord(t[i]) - ord('a')
            
            # print(f"{start=} {end=}")
            
            left_cost = 0
            right_cost = 0
            
            if start < end:
                left_cost = sum(previousCost[start :: -1] + previousCost[25 : end: -1])
                right_cost = sum(nextCost[start:end])
            else:
                left_cost = sum(previousCost[start : end: -1])
                right_cost = sum(nextCost[start:] + nextCost[:end])
                

            # print(f"{left_cost=} {right_cost=}")
            min_cost += min(left_cost, right_cost)
            i+=1
            # j+=1

        return min_cost
            
                    