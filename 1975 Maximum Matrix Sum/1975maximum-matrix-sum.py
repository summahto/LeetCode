class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # heap = []
        min_num = float('inf')
        num_negatives= 0
        total = 0

        for i in range(m):
            for j in range(n):

                total += abs(matrix[i][j])
                min_num = min(abs(matrix[i][j]), min_num)
                # heapq.heappush(heap, abs(matrix[i][j]))
                
                if matrix[i][j] < 0:
                    num_negatives += 1

        
        if num_negatives %2 == 0:
            return total
        

        return total - (2* min_num)