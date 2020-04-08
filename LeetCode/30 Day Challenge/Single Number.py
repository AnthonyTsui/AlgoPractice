# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4


#Two approaches: We can use a hash table in order to store lal the occureances of each element we've sen
#This requries O(N) time and O(N) space, the other approach is to utilize bit maniputation
#We do this with the XOR operator, and we XOR every element in the array with 0. Each duplicate element will cancel each other out,
#and then we just need to returns ans as 0 xor num = num

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans
        
        #O(N) time and space complexity, utilize a hash table in order to storer 
        #all the values we've seen so far and then iterate through the hash table again,
        #in order to see which value we've only seen once
        
        # seenValues = {}
        # for num in nums:
        #     if num not in seenValues:
        #         seenValues[num] = 0
        #     seenValues[num] += 1
        # for num, freq in seenValues.items():
        #     if freq == 1:
        #         return num