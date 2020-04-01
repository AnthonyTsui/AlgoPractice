# Given an integer array, you need to find one continuous subarray that 
# if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.


#Approach: Find the smallest and largest number out of place, as this will determine the boundaries of our unsorted subarray
#Traverse the array two more times to find the index of the first number greater than our smallest unsorted element, and the index of the 
#last number smaller than our greatest unsorted element
#Time complexity: O(N) and spce complexity is O(1)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0 
        if len(nums) == 1: return 0
        
        leftUnsorted, rightUnsorted = float("inf"), float("-inf")
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                leftUnsorted = min(nums[i], leftUnsorted)
                rightUnsorted = max(nums[i-1], rightUnsorted)
        if leftUnsorted == float("inf"): return 0
        
        leftIndex, rightIndex = 0, 0
        for i in range(len(nums)):
            if nums[i] > leftUnsorted:
                leftIndex = i
                break
        for i in reversed(range(len(nums))):
            if nums[i] < rightUnsorted:
                rightIndex = i
                break
        return rightIndex - leftIndex + 1