# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# # 

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

#Time complexty:  O(N^2)
#Space Complexity:O(N), as that is the largest all call stackk will grow


from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def getPerm(nums, curr, res):
            if nums == []:
                res.append(curr)
                return;
            seen = set()
            for i,x in enumerate(nums):
                if x not in seen:
                    getPerm(nums[:i]+nums[i+1:], curr+[nums[i]], res)
                    seen.add(x)
        getPerm(nums, [], res)
        return res
                