# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
#  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

#Time complexity: O((w*h)^2) where w = width of the grid and h = height of the grid , in a grid with all 1s we would be checking all of these 
#Space complexity O(w*h)

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        checkedCells = [[False for j in range(len(grid[i]))] for i in range(len(grid))]
        
        def checkNeighbors(row, col, grid):
            width = len(grid[0])
            height = len(grid)
            output = []
            if row > 0:
                output.append([row-1, col])
            if row < len(grid)-1:
                output.append([row+1, col])
            if col > 0:
                output.append([row, col-1])
            if col < len(grid[0])-1:
                output.append([row, col+1])
            return output
                
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if checkedCells[row][col]:
                    continue
                checkedCells[row][col] = True
                if grid[row][col] == "0":
                    continue
                islands += 1
                stack = [[row, col]]
                while stack:
                    curr = stack.pop()
                    checkedCells[curr[0]][curr[1]] = True
                    if grid[curr[0]][curr[1]] == "1":
                        grid[curr[0]][curr[1]] = "0"
                        stack.extend(checkNeighbors(curr[0], curr[1], grid))
        return islands