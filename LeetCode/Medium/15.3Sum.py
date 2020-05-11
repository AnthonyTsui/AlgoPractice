# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

#Approach: We need to check every combination of 3 numbers from the array
#To make this more efficient, we'll sort the array and iterate through 0 -> len(nums)-2, with left,right = i+1, len(nums)-1
#Couple of things to note here: since the array is sorted, if our left most number (nums[i]) >0, then we can exit the loop as this means all other numbers are >0 
#There may also be duplicates in our nums, not just in i, i+1... but also in ourleft, right which will result in us giving duplicate responses.
#The naive approach would be to utilize a set() in order to keep track of the combinations we've seen so far.
#The more efficient method is to check our left, right, and i numbers each time we seen a viable combination and iterate them until they are pointing to a different number

#Time complexity: O(N^2) while it is O(NlogN) + O(N^2) = ~ O(N^2). We sort for nlogn time and also iterate through the array N times, each time iterating through n-1 time so O(N^2)
#Space Complexity: O(1) if we're not counting the answer list. OTherewise, O(N) for storing the combinatins (or N)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            left, right = i+1, len(nums)-1
            while left < right:
                curr = nums[left] + nums[right] + nums[i]
                if curr < 0:
                    left += 1
                elif curr > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return answer