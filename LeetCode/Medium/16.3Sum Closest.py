# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

# Constraints:

# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(len(nums)-2):
            curr = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                currSum = curr + nums[left] + nums[right]
                if currSum == target: return target
                res = res if abs(res - target) < abs(currSum - target) else currSum
                if currSum > target:
                    right -= 1
                else:
                    left += 1
        return res
                