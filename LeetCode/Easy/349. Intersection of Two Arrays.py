# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]

#Time Complexity: O(N+M) where N = len(nums1), M = len(nums2)
#Space Complexity: O(N+M)

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        
        if len(set1) > len(set2):
            return [n for n in set2 if n in set1]
        else:
            return [n for n in set1 if n in set2]
        
        
        # set1, set2 = set(nums1), set(nums2)
        # return list(set1 & set2)
    
        # seen = set(nums1)
        # ans = set()
        # for n in nums2:
        #     if n in seen: ans.add(n)
        # return ans
            