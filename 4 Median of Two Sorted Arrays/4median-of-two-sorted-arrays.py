class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1 = len(nums1)
        n2 = len(nums2)

        idx1 = (n1 + n2)//2
        idx2 = (n1 + n2)//2 -1
        elem1, elem2 = 0,0
        
        i, j, k = 0, 0, 0
        
        # def setMidElements(arr : list[int], idx):
        #     e1, e2 = 0,0
        #     if idx1 == k:
        #         e1 = arr[idx]
        #     if idx2 == k:
        #         e2 = arr[idx]
            
        #     return e1, e2

        while i< n1 and j < n2 and k != idx1 +1:
            if nums1[i] < nums2[j]:
                # elem1, elem2 = setMidElements(nums1, i)
                if idx1 == k:
                    elem1 = nums1[i]
                if idx2 == k:
                    elem2 = nums1[i]
                i+=1
                
            else :
                # elem1, elem2 = setMidElements(nums2, j)
                if idx1 == k:
                    elem1 = nums2[j]
                if idx2 == k:
                    elem2 = nums2[j]
                j+=1
            
            k+=1

        while i< n1 and (k) != idx1 +1:
            # elem1, elem2 = setMidElements(nums1, i)
            if idx1 == k:
                elem1 = nums1[i]
            if idx2 == k:
                elem2 = nums1[i]
            
            i+=1
            k+=1
        
        while j< n2 and (k) != idx1 +1:
            # elem1, elem2 = setMidElements(nums2, j)
            if idx1 == k:
                elem1 = nums2[j]
            if idx2 == k:
                elem2 = nums2[j]
            j+=1
            k+=1

        if (n1 + n2)%2 != 0:
            return elem1

        print(elem1, elem2, idx1, idx2)
        return (elem1 + elem2) /2.0
        

        
 