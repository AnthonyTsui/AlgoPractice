# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

#Approach: We can use the DFS approach, where we just take the currSum, and fork here with currSum + (currElem) and currSum - (currElem)
#This ends up being 2^n time complexity, but we can reduce this time by using memoization so that subproblems we have solved before have constant look up time.

#Time complexity: O(L*N) where L is the range of currSum, and N is the number of elements
#Space eComplexity: O(L*N) 

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.memo = {}
        return self.dP(nums, S, 0, 0)

        
    def dP(self, nums, target, index, currSum):
        if (index, currSum) in self.memo:
            return self.memo[(index, currSum)]
        
        if index == len(nums):
            if currSum == target:
                return 1
            return 0
        
        positive = self.dP(nums, target, index+1, currSum + nums[index])
        negative = self.dP(nums, target, index+1, currSum - nums[index])
        
        self.memo[(index, currSum)] = positive +negative 
        return self.memo[(index, currSum)]