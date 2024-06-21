class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)

        if (m * k) > n:
            return -1

        lo, hi = min(bloomDay), max(bloomDay)

        def numOfBouq(days):
            streak = 0
            ans = 0
            i = 0
            while i < n :
                if bloomDay[i] <= days:
                    streak += 1
                else :
                    streak = 0
                
                if streak == k:
                    ans += 1
                    streak = 0
                i+=1
                
            # print(mid, ans)

            return ans

        while lo < hi:
            mid = (lo + hi) //2
            total = numOfBouq(mid)

            if total < m:
                lo = mid +1
            else:
                hi = mid
        
        return lo