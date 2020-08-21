# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


#Time Complexity :O(logN) as nums is already sorted and our binSearch operation takes log(n) time 
#Space Complexity: O(1)

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(nums, target, left):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (hi+lo)//2
                if nums[mid] > target or (left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid+1
                    
            return lo
        left = binSearch(nums, target, True)
        
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, binSearch(nums, target, False)-1]