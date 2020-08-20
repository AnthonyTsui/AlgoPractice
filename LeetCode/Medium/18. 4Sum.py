# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(l, r, target, n, combination, res):
            if r-l+1 < n or n < 2 or target < nums[l]*n or target > nums[r]*n:
                return
            if n == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(combination+[nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i] != nums[i-1]):
                        kSum(i+1, r, target-nums[i], n-1, combination + [nums[i]], res)
        
        nums.sort()
        res = []
        kSum(0, len(nums)-1, target, 4, [], res)
        return res

            
#         combinations = collections.defaultdict(list)
#         nums.sort()
#         res = []
#         for i in range(1, len(nums)-1):
#             currNum = nums[i]
#             for k in range(i+1, len(nums)):
#                 remaining = target - (nums[k] + nums[i])
#                 for pair in combinations[remaining]:
#                     comb = [nums[k], nums[i]] + pair
#                     if comb in res: 
#                         continue
#                     res.append([nums[k], nums[i]] + pair)
#             for j in range(i):
#                 pairSum = nums[i] + nums[j]
#                 combinations[pairSum].append([nums[i], nums[j]])
            
#         return res