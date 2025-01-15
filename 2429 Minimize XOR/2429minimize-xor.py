class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        binNum2 = bin(num2)[2:]
        setBitsNum2 = binNum2.count('1')

        binNum1 = bin(num1)[2:]
        setBitsNum1 = binNum1.count('1')

        if setBitsNum2 == setBitsNum1:
            return num1

        ans = []
        if setBitsNum1 > setBitsNum2:
            # place these set bits at the msb of n1
            count = 0
            for i, c in enumerate(binNum1):

                if count < setBitsNum2:
                    ans.append(c)
                else:
                    ans.append('0')
    
                if c  == '1': 
                    count+= 1

        
            binAns = ''.join(ans)
            # print(binAns)
            
            return int(binAns, 2)

        res= list(binNum1)
        # print(res)
        if setBitsNum1 < setBitsNum2:
            #  place the number of 'setBitsNum1' bits at the same positions as the num1
            # and the remaining at the LSB positions
            count = setBitsNum1
            n = len(res)

            for i in range(n-1, -1, -1):
                if count == setBitsNum2:
                    break
    
                if res[i] == '0':
                    res[i] = '1'
                    count+= 1
            
            while count < setBitsNum2:
                res.insert(0, '1')
                count += 1

        result = list(res)

        return int((''.join(result)), 2)