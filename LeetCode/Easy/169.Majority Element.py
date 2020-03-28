# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Boyer-Moore Voting Algorithm: Time Complexity: O(N) Space Complexity: O(1)
        candidate = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
                
        
        
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
#         nums.sort()
#         mid = len(nums)//2
#         return nums[mid]
        
        # dict = {}
        # for num in nums:
        #     if num not in dict:
        #         dict[num] = 0
        #     dict[num] += 1
        #     if dict[num] >= float(len(nums))/2:
        #         return num
        
        