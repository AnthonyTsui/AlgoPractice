# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

# Return the length of the longest (contiguous) subarray that contains only 1s. 

 

# Example 1:

# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
# Example 2:

# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

#Time COmplexity:O (N)
#Space Complexity:O(1)
from typing import List
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0 
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j -i + 1