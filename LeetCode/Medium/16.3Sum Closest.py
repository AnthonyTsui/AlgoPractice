# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

# Constraints:

# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

#First sort the nums array 
#Iterate through each number in the list and for each ith number, set two points: one at i+1 and one at the end of the array
#Iterate the two pointers, with the left increasing and the right decreasing. We check the current sum of the numbers located at i and our two pointers
#and compare them to our current closest number. If it is equivalent we simply return it, otherwise we check to see if it is closer.
# 
# We can optimize this slightly but skipping repeated numbers, as we would have checked them already.

# Time complexity is O(N^2), as O(nlogn) for sorting and O(n^2) for our two-pointer iteration
# Space complexity is O(1) as we only ever store a static number of variables at a time 
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(len(nums)-2):
            curr = nums[i]
            left, right = i+1, len(nums)-1
            if i > 0 and nums[i-1] == nums[i]:
                continue
            while left < right:
                currSum = curr + nums[left] + nums[right]
                if currSum == target: return target
                res = res if abs(res - target) < abs(currSum - target) else currSum
                if currSum > target:
                    right -= 1
                else:
                    left += 1
        return res
                