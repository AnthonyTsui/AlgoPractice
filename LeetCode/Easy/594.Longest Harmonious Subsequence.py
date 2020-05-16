# We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

# Example 1:

# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

#Time Complexity: O(N)
#Space Complexity: O(n) where n = number of unique elements in the list 

import collections

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        freq = collections.Counter(nums)
        res = 0
        
        for num in freq.keys():
            if num+1 in freq:
                res = max(res, freq[num]+freq[num+1])
        return res