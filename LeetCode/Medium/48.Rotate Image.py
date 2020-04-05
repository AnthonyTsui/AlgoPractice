# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Example 2:

# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 

# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

#Approach: Notice that we can a general formula where if we iterate through all the elements in the top left quadrant of a matrix, we can 
#use the coordinates to the find other three elements that we need to swap with. Then we can simply use pythons assignment syntax to swap them all in place.

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(len(matrix)//2):
            for j in range(i, (n-i-1)):
                matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = \
                    matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]
                    
                
                #Don't do the below, I was just trying to figure the formula out but it may be helpful for seeing the thought process
                
                # temp = matrix[j][len(matrix)-i-1]
                # matrix[j][len(matrix)-i-1] = matrix[i][j]
                # matrix[len(matrix)-i-1][len(matrix)-j-1], temp = temp,  matrix[len(matrix)-i-1][len(matrix)-j-1]
                # matrix[len(matrix)-j-1][i], temp = temp, matrix[len(matrix)-j-1][i]
                # matrix[i][j] = temp
        return matrix