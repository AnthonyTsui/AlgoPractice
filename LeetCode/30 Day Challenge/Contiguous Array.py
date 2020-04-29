# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


#Approach: We can visualize the trend of the binary array using a variable count that starts at 0.
#We +1 to count if num == 1 and -1 if num == 0. Note that when we encounter an value for 'count' multiple times, it means there is an equal number of 0s and 1s
#since we last encountered that count value. We can use this by keeping a hashmap of the count as well as the index we first encountered it at, and 
#recalculate the maximum length of the largest contiguous subarray whenever we recounter that count.

#Time complexity O(N) as we only iterate through the array nums once
#Space complexity: O(N) as we may potentially store all the indexes in nums (say for example they are all 1s or all 0s)

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapping = {0:-1}
        count = 0 
        maxLen = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in mapping:
                maxLen = max(maxLen, i - mapping[count])
            else:
                mapping[count] = i
        return maxLen
            