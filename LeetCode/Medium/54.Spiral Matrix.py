# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

#Time Complexity: O(N*M)
#Space Complexity: O(N*M)

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        if len(matrix) == 1: return matrix[0]
        
        def get_coords(r1, r2, c1, c2):
            for c in range(c1, c2+1):
                yield r1, c
            for r in range(r1+1, r2+1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2-1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1         
        
        res = []
        w, h = len(matrix[0]), len(matrix)
        r1,r2 = 0, h-1
        c1, c2 = 0, w-1
        while r1 <= r2 and c1 <= c2:
            for r,c in get_coords(r1, r2, c1, c2):
                res.append(matrix[r][c])
            r1 +=1; r2 -= 1
            c1 +=1; c2 -= 1
        return res
        
        
        