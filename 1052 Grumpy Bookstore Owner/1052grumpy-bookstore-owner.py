class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        conMinSum = 0
        total = 0


        for i in range(n):
            if grumpy[i] == 0:
                total += customers[i]

        loss, j = 0 , 0
        maxLoss = 0
        
        # print("i outside while = ", i)
        i = 0

        while i< minutes:
                if grumpy[i] == 1:
                    loss += customers[i]
                i+=1

        maxLoss = max(maxLoss, loss)

        while i < n:
            
            # print("i = ", i)
            
            if grumpy[j] == 1 :
                loss -= customers[j]
            if grumpy[i] == 1:
                loss += customers[i]
            
            # print(f'i = {i} : {maxLoss}, {loss}')
            j+= 1
            i+= 1
            maxLoss = max(maxLoss, loss)
            

        return total + maxLoss



