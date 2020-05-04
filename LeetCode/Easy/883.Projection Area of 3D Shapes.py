# On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

# Now we view the projection of these cubes onto the xy, yz, and zx planes.

# A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

# Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

# Return the total area of all three projections.

 

# Example 1:

# Input: [[2]]
# Output: 5
# Example 2:

# Input: [[1,2],[3,4]]
# Output: 17

#Time complexity :O(N^2)
#Space complexity: O(N) where N = len(grid)

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        answer = 0
        answer += len(grid)*len(grid)
        
        yMax = [0 for y in range(len(grid))]

        for row in grid:
            answer += max(row)
            for i in range(len(row)):
                yMax[i] = max(yMax[i], row[i])
                if row[i] == 0: answer -= 1
            
        
        return answer + sum(yMax)