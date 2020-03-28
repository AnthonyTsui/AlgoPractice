# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

#Time complexity: O(3N) 
#71.65% Time and 5.06% Space

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        while left < len(nums) and nums[left] != 0:
            left += 1
        right = left + 1
        while right < len(nums) and nums[right] == 0:
            right += 1
        while left < len(nums) and right < len(nums):
            if nums[left] == 0:
                nums[left], nums[right] = nums[right],nums[left]
            while right < len(nums) and nums[right] == 0:
                right += 1
            left += 1
        return nums
