class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0 # left ptr: keeps track of 1st elem of longest subarray with 3 dist. elem (abc) 
        m = 0 # middle pointer: keeps track of 1st element with shortest subarray of length 3
        r = 0 
        count = 0
        n = len(s)
        freqMap = defaultdict(int)

        while r< n:
            freqMap[s[r]] += 1

            # if the count of the mid ptr is greater than 1 then we know this is not the shortest subarray of length 3, hence we move it forward and run it until we don't see smallest possible subarray of length 3
            while freqMap[s[m]] > 1:
                freqMap[s[m]] -= 1
                m += 1

            if len(freqMap) == 3:
                count += (m - l + 1)

            r+= 1

        return count