class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l, m, r = 0, 0, 0
        n = len(nums)

        count = 0
        freqMap = defaultdict(int)

        while r < n:
            freqMap[nums[r]] += 1

            while len(freqMap) > k and m<= r:
                freqMap[nums[m]] -= 1

                if freqMap[nums[m]] == 0:
                    del freqMap[nums[m]]

                m += 1
                l = m

            while freqMap[nums[m]] > 1:
                freqMap[nums[m]] -= 1
                m += 1

            if len(freqMap) == k:
                count += (m -l + 1)

            # print(count, l, m, r)
            r +=1

        

        return count