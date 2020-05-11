# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true
# Example 2:

# Input: [1,2,3,4]
# Output: false
# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true


#Approaches: Use a hashmap and check if we've seen the current value before
#Using python, covert nums to a set (O(N)) and compare the lengths of the set and original list


#TIme Complexity: O(N)
#Space COmplexity:O(N) [or O(1) if you used the set approach]

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # freq = {}
        # for num in nums:
        #     if num in freq: 
        #         return True
        #     freq[num] = 1
        # return False
        
        return len(nums) > len(set(nums))
        
        
        #With no extra space but modifies the nums array
#         if len(nums) <= 1: return False
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
#         return False
        