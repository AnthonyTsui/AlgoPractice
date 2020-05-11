# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

#Time Complexity: O(N)
#Space Complexity: O(1)

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = nums[0]
        runningMax = runningMin = currMax
        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp = runningMax
                runningMax = runningMin
                runningMin = temp
            runningMax = max(nums[i], nums[i]*runningMax)
            runningMin = min(nums[i], nums[i]*runningMin)
            
            currMax = max(currMax, runningMax)
            
        return currMax