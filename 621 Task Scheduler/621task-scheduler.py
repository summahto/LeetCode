class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Solution 1
        
        freq = [0] *26

        for c in tasks:
            freq[ord(c) - ord('A')] += 1

        freq.sort()
        maxFreq = freq[25] -1 # num of gaddhe
        idleSlots = maxFreq * n 

        for i in range(24, -1, -1):
            idleSlots -= min(maxFreq, freq[i]) # min(num of gaddhe, freq[i])

        
        if idleSlots > 0:
            return len(tasks) + idleSlots
        
        return len(tasks)