# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.


#Approach: We can use dynamic programming to keep track of the minimum path.
#We know that every element except for the top row and left column has two choices for a minimum path: go from the above element go from the element to the right.
#We can then set our left column and top row values, then traverse from grid[1][1]. We set the value grid[i][j] to the minimum value of [i-1][j] (top value) or
#[i][j-1] (left value) and add the current number to that minimum value. The result then is that we take the minimum path each time, and when we arrive to our 
#destination, [-1][-1], the two choices are already at their minimum. 

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
 #If we don't care about mutating our grid and just want the result: Time Complexity O(w*h), Space Complexity O(1)

        width = len(grid[0])
        height = len(grid)
        for i in range(1, width):
            grid[0][i] += grid[0][i-1]
        for i in range(1, height):
            grid[i][0] += grid[i-1][0]
        for i in range(1, height):
            for j in range(1, width):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]) 
        return grid[-1][-1]

#Only creating two lists with the width of our grid, better space complexity, same time complexity
#         if len(grid) == 1: return sum(grid[0])
        
#         prev = [elem for elem in grid[0]]
#         for i in range(1, len(prev)):
#             prev[i] += prev[i-1]
            
#         curr = [0 for elem in grid[0]]
#         curr[0] = grid[1][0] + grid[0][0]
        
#         row = 1
#         while row < len(grid):
#             for j in range(1, len(curr)):
#                 curr[j] = min(curr[j-1], prev[j]) + grid[row][j]
#             if row == len(grid)-1:
#                 break
#             prev = curr
#             curr[0] = prev[0] + grid[row+1][0]
#             row += 1
#         return curr[-1]



#Creating a whole new grid to store our results

#         minPaths = [[elem for elem in grid[i]]for i in range(len(grid))]
#         for i in range(1, len(minPaths[0])):
#             minPaths[0][i] += minPaths[0][i-1]
#         for i in range(1, len(minPaths)):
#             minPaths[i][0] += minPaths[i-1][0]
#         for i in range(1, len(minPaths)):
#             for j in range(1, len(minPaths[0])):
#                 minPaths[i][j] = min(minPaths[i-1][j], minPaths[i][j-1]) + grid[i][j]
#         return minPaths[-1][-1]