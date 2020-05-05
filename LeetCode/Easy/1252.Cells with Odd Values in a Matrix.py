# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

# Return the number of cells with odd values in the matrix after applying the increment to all indices.

 

# Example 1:


# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
# Example 2:


# Input: n = 2, m = 2, indices = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.

#Approach: Main take away is return ((m-oddCols)*oddRows) + ((n-oddRows)*oddCols), everything else is pretty self explanatory
#Time complexity: O(i) where i = len(indices), more specifically this should be O(i + m + n) but i < m or n so we cna define it as a O(x*i)
#Space Complexity: O(m + n)
import collections

class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        if not indices: return 0
        rows, cols = collections.Counter(), collections.Counter()
        for i in indices:
            row, col = i[0], i[1]
            rows[row] += 1
            cols[col] += 1
#             if row not in rows:
#                 rows[row] = 0
#             rows[row] += 1
            
#             if col not in cols:
#                 cols[col] = 0
#             cols[col] += 1
            
        oddRows = sum(map(lambda x: x%2 == 1, rows.values()))
        oddCols= sum(map(lambda x: x%2 == 1, cols.values()))
        
        return ((m-oddCols)*oddRows) + ((n-oddRows)*oddCols)
    
    
