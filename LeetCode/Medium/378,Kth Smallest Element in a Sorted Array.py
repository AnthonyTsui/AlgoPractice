# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.


from heapq import * 

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(min(len(matrix), k)):
            heappush(heap, (matrix[i][0], 0, matrix[i]))
        count = 0
        while heap:
            num, col, row = heappop(heap)
            count += 1
            if count == k:
                break
            if col+1 < len(row):
                heappush(heap, (row[col+1], col+1, row))
            
        
        return num