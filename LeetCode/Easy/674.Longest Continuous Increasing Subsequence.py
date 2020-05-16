# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
# Note: Length of the array will not exceed 10,000.

#Time Complexity: O(N)
#Space Complexity:O(1)

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = left = 0
        
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]:
                left = i
            ans = max(ans, i - left+ 1)
        return ans 
        
        
#         if not nums: return 0
#         res, currLength, currNum = 1, 1, nums[0]
        
#         for num in nums:
#             if num > currNum:
#                 currLength += 1
#                 res = max(res, currLength)
#             else:
#                 currLength = 1
#             currNum = num
#         return res
        