# Students are asked to stand in non-decreasing order of heights for an annual photo.

# Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

# Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.

 

# Example 1:

# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# Current array : [1,1,4,2,1,3]
# Target array  : [1,1,1,2,3,4]
# On index 2 (0-based) we have 4 vs 1 so we have to move this student.
# On index 4 (0-based) we have 1 vs 3 so we have to move this student.
# On index 5 (0-based) we have 3 vs 4 so we have to move this student.
# Example 2:

# Input: heights = [5,1,2,3,4]
# Output: 5
# Example 3:

# Input: heights = [1,2,3,4,5]
# Output: 0


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        answer = 0
        
        maxNum = max(heights)
        freq = [0]*(maxNum+1)
        sumCount = [0]*(maxNum+1)
        
        for height in heights:
            freq[height] += 1
        
        for i in range(1, len(sumCount)):
            sumCount[i] = freq[i] + sumCount[i-1]
        
        curr = 0
        sortedHeights = []
        
        for i, val in enumerate(sumCount):
            sortedHeights.extend([i]*(val-curr))
            curr = val
        
        for i in range(len(sortedHeights)):
            if sortedHeights[i] != heights[i]:
                answer += 1

        return answer
#         sortedHeights = sorted(heights)                     
#         moved = 0
#         for i in range(len(heights)):
#             if heights[i] != sortedHeights[i]:
#                 moved += 1
        
#         return moved