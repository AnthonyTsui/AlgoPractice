# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

 

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:

# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:

# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
 

# Constraints:

# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

#Approach: Sorting the list lets us check all the smaller elements of each number in nLogn time for the sort,
#and N time for a single pass.

#Time Complexity: O(NLogN) where N is the number of elements in nums 
#Space complexity: O(N)

import collections

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        
        sorted_nums = sorted(nums)
        mapping = collections.defaultdict(list)
        smaller = 0
        mapping[sorted_nums[0]] = 0
        
        for i in range(1, len(sorted_nums)):
            curr = sorted_nums[i]
            smaller += 1
            
            if curr == sorted_nums[i-1]:
                continue
            else:
                mapping[curr] = smaller
        
#         answer = []
#         for num in nums:
#             answer.append(mapping[num])
            
#         return answer
    
        return [mapping[num] for num in nums]
        
        