# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

#Approach: We start with our output array havng only the empty set [] such that output = [[]]
#We know that every singular element in our nums array is a subset of the powerset.
#We can achieve this by iterate through each number and append it to the empty set and adding it to our powerset.
#This means we need to perform [].append(num) for every num in nums.
#To streamline this, we know that after one element ,we get [],[1] in our powerset. we can then simply call the next element on our entire power set to achieve the next combination of 
#subsets. [[],[1]] -> combine with [2] -> [[],[1],[2],[1,2]] and so on.

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        allSubsets = [[]]
        for num in nums:
            for i in range(len(allSubsets)):
                curr = allSubsets[i][:]
                curr.append(num)
                allSubsets.append(curr)
        return allSubsets