class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        arr = sentence.split(' ')
        n = len(arr)
        
        if arr[0][0] != arr[n-1][-1]:
            return False

        for i in range(1, n):
            # print(f"{arr[i]=} {arr[i-1]=}")
            if arr[i][0] != arr[i-1][-1]:
                return False
        
        return True
