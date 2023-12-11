class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        if len(arr) == 1:
            return arr[0]
    
        maxCount, count = 0, 1
        if len(arr) % 4 != 0:
            moreThan25 = math.ceil(len(arr) / 4)
        else :
            moreThan25 = (len(arr)/4) +1 
        # print(moreThan25)

        i = 1
        while i < len(arr):
            if arr[i] != arr[i-1]:
                count = 1
            else: 
                count +=1
                if count >= moreThan25:
                    break
            i+=1

        return arr[i]
            
            

