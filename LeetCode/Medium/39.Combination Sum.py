# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

#Approach: We need to check every combination of number (including a number with itself), this follows a depth first search question, where we go as far as 
#possible with our current element and explore all possible routes in this path, and in those paths. We can incorporate a DFS, without exit case being if 
#we reach our target sum (curr == 0) in our current path, or if we go past our target sum(in which case it is not a valid path)

#Time complexity: We traverse the array O(N) times and call dfs on each individual one, meaning N*N-1*N-2..meaning the time complexity = O(N^2)
#Space complexity: O(N^2) as well? Based on the call stack

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        dfs(candidates, 0, target, [], output)
        return output
        
def dfs(candidates, index , target, path, output):
    if target < 0 :
        return
    if target == 0:
        output.append(path)
        return
    for i in range(index, len(candidates)):
        dfs(candidates, i,  target-candidates[i], path+[candidates[i]], output)
                               
                            