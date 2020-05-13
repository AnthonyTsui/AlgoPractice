# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:

# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:

# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

#         is_col = False
        
#         for i in range(len(matrix)):
#             if matrix[i][0] == 0 :
#                     is_col = True
#             for j in range(1,len(matrix[0])):    
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = 0
#                     matrix[0][j] = 0

#         for i in range(1, len(matrix)):
#             for j in range(1, len(matrix[0])):
#                 if not matrix[i][0] or not matrix[0][j]:
#                     matrix[i][j] = 0

#         if matrix[0][0] == 0:
#             matrix[0] = [0]*len(matrix[0])
        
#         if is_col:
#             for row in range(len(matrix)):
#                 matrix[row][0] = 0
        
#         return matrix
        
        
        seenCols = set()
        
        for i in range(len(matrix)):
            seenZeros = []
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    seenZeros.append(j)
                    for row in range(0, i+1):
                        matrix[row][j] = 0
                if j in seenCols:
                    matrix[i][j] = 0
            if len(seenZeros) > 0:
                matrix[i] = [0]*len(matrix[0])        
            seenCols.update(seenZeros)
        return matrix
                    
                    
            
                
        
        
        
        #Time Complexity: O(h*w)
        #Space Complexity: O(h*w)
#         seenZeros = []
        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j] == 0:
#                     seenZeros.append((i, j))
        
#         while seenZeros:
#             x, y = seenZeros.pop()
#             matrix[x] = [0]*len(matrix[0])
#             for i in range(len(matrix)):
#                 matrix[i][y] = 0
                
#         return matrix