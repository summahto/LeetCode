class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo = 1
        hi = max(quantities)

        def check_distr_possible(x: int):
            available = sum(quantities)
            stores = 0

            for q in quantities:
                
                stores += ceil(q/x)
                # while q >= x:
                #     available -= x
                #     stores+= 1
                #     q -= x
                
                # if q > 0:
                #     stores += 1
                #     available -= q
                #     q = 0

                # print(f"{available=} {q=} {stores=}")
                if stores > n:
                    return False

            # after assigning max of 'x' products , if there are still some products remaining, that means the x is not eenough x should be higher
            return True


        while lo < hi:
            mid = (lo + hi)//2
            
            # print(mid)
            
            if check_distr_possible(mid):
                # distribution is possible, you can find a lower value
                hi = mid
            else :
                # distribution not possible, 
                lo = mid +1
            

        return lo