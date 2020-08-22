# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?
# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right


#Time Complexity: O(m*n)
#Space Complexity: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1 for w in range(m)] for h in range(n)]
        for r in range(1, len(paths)):
            for c in range(1, len(paths[0])):
                paths[r][c] = paths[r-1][c] + paths[r][c-1]
        return paths[-1][-1]