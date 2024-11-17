class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        i, j = 0, n-1

        # find the indices of the left sorted part and the right sorted part
        while i < n-1 and arr[i] <= arr[i+1]:
            i+=1
        
        while j > 0 and arr[j] >= arr [j-1]:
            j-= 1
        
        # i crossed j => arr in asc order
        # the = case is when we have only one element in the array
        if i >= j:
            return 0
        
        # initialize min_len with the whole left side (left sorted part + unsorted part) of the array 
        # min_len = j

        # if set to either of min(total - left, total - right), then check # 39 is not required
        min_len = min(j, n - i -1)

        left = 0
        right = j

        # print(f"{i=} {j=}")

        # go from 0 -> i (largest element of left sorted part) and try to merge with the right sorted part
        # merge ?? how ?? 
        while left <= i and right < n:
            
            while right < n and arr[left] > arr[right]:    
                right += 1

            
            min_len = min(min_len, (right- left -1))
            left += 1

        # Required in case, we have already consumed all of the right sorted part, but the left sorted part is larger than the right one.
        # 39
        # while left <= i:
        #     min_len = min(min_len, (right - left -1))
        #     left +=1 

        return min_len
                