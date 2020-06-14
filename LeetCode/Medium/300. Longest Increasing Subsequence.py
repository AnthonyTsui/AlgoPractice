# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.

#Time Complexity: O(N^2)
#Space Complexity: O(N)

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxLen = [0]*len(nums)
        maxLen[0] = 1
        ans = 1
        
        for i in range(1, len(nums)):
            maxval = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, maxLen[j])
            maxLen[i] = maxval+1
            ans = max(maxLen[i], ans)
        return ans