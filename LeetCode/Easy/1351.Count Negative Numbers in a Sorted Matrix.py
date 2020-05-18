# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

# Return the number of negative numbers in grid.

 

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0
# Example 3:

# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
# Example 4:

# Input: grid = [[-1]]
# Output: 1

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width, height = len(grid[0]), len(grid)
        row, col, ans = height-1, 0 , 0
        
        while row >= 0 and col < width:
            if grid[row][col] < 0:
                ans += width - col
                row -= 1
            else:
                col += 1
        return ans
                
                
        
#         width, height = len(grid[0]), len(grid)
#         ans = 0
#         for i in range(height):
#             if grid[i][0] < 0:
#                 return ans + (width * (height-i))
#             for j in range(width):
#                 if grid[i][j] < 0:
#                     ans += width - j
#                     break
#         return ans
                
                