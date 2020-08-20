# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


#Essentially we either i-th position element, we want to see
#ith + [every permutation of i-th element]
#and then take that array, and apply the same concept to the ith+1 element

#An iterative approach would be to add numbers one at a time, and each time we add a new number
#we swap the new number with every other number already added and save each of these swapped instances, as they are our permutations
#Example) [1,2,3]
#[]
#Add 1 : [] -> [1]
#Add 2: [1]  -> Now swap our new num (2) with all the other numbers including itself (so we can save itself) -> save([1,2])  save ([2,1])
#Add 3: [[1,2],[2,1]] -> [1,2,3] -> [1,3,2], [3,2,1] and [2,1,3] -> [3,1,2], [2,3,1] 
#Final result: [1,2,3] [1,3,2] [3,2,1] [2,1,3] [3,1,2] [2,3,1] 
# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         permutations = [[]]
#         for num in nums:
#             newPermutations = []
#             for i in range(len(permutations)):
#                 currPermutation = permutations[i]
#                 currPermutation.append(num)
#                 for j in range(len(currPermutation)):
#                     currPermutation[-1], currPermutation[j] = currPermutation[j], currPermutation[-1]
#                     newPermutations.append(currPermutation[:])
#                     currPermutation[-1], currPermutation[j] = currPermutation[j], currPermutation[-1]
#             permutations = newPermutations
#         return permutations

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        def helper(i, nums, permutations):
            if i == len(nums)-1:
                permutations.append(nums[:])
            else:
                for j in range(i, len(nums)):
                    swap(nums, i, j)
                    helper(i+1, nums, permutations)
                    swap(nums, i, j)
        helper(0, nums, permutations)
        return permutations
        
        # n = len(nums)
        # res = []
        # def dfs(l):
        #     if l ==  n-1:
        #         res.append(list(nums))
        #         return
        #     for i in range(l, n):
        #         nums[l], nums[i] = nums[i], nums[l]
        #         dfs(l+1)
        #         nums[l], nums[i] = nums[i], nums[l] 
        # dfs(0)
        # return res
                
#123

#123 -> 123 ->123 res add 123
# 132 -> res add 132 -> back to 123
#213 -> 213 -> add 213 -> 231 -> add 231 -> back to 213
#etc..