# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false


#Approach: We know that the rows are both sorted horizontally and vertically. this means matrix[-1][-1] has the largest possible value and matrix[0][0] is the smallekst possible value
#This also means that within a row, all elements are > row[0] and < row[-1]. We can set a starting point to be either the top right or bottom left,
#as this situates us in a position where we can decide to traverse the column or row based on our current value
#In the case of top right: if the value is smaller than our curr, we move down to a larger number. if the value is larger than our curr, we move left to a smaller number.
#Using this approach we will always find our value if it exists, otherwise we go out of bounds and return false

#Time complexity: O(w+h) we may traverse from one corner to the toher just to find it does not exist
#Space complexity: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]): return False
        col, row = len(matrix[0]) - 1, 0
        while row < len(matrix) and col >= 0:
            if target == matrix[row][col]:
                return True
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
        return False
        