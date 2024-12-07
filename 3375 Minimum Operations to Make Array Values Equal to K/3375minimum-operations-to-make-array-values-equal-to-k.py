class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        c = Counter(nums)
        freq = sorted(c.items())
        # print(f"{freq=}")

        first = next(iter(freq))

        if k > first[0]:
            return -1
            
        n = len(freq)

        if k == first[0]:
            return n-1

        return  n
        