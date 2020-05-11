# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

#Approach: Utilize a hashmap to store the value as a key and the index as the value
#Store all the nums as we see them and check if the "remaining" value has been seen

#Time Complexity :O(N)
#Space Complexity: O(N) since we may store the entire nums array


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        mapping = {}
        for i,num in enumerate(nums):
            remaining = target - num
            if remaining in mapping: return [mapping[remaining], i]
            mapping[num] = i
        return [0, 0]