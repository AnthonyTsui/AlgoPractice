# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

 

# Example 1:

# Input: [1,2,2,3]
# Output: true
# Example 2:

# Input: [6,5,4,4]
# Output: true
# Example 3:

# Input: [1,3,2]
# Output: false
# Example 4:

# Input: [1,2,4,5]
# Output: true
# Example 5:

# Input: [1,1,1]

#Time Complexity: O(N)
#Space Complexity:O(1)

from typing import List
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # increasing = decreasing = True
        # for i in range(len(A)-1):
        #     if A[i] > A[i+1]:
        #         increasing = False
        #     if A[i] < A[i+1]:
        #         decreasing = False
        # return increasing or decreasing
        
        
        if len(A) <= 1: return True
        curr, inc = A[0], None
        for i in range(1, len(A)):
            if curr == A[i]:
                continue
            if inc is None:
                if curr > A[i]: inc = False
                else: inc = True
                curr = A[i]
                continue
            if curr > A[i] and inc:
                return False
            elif curr < A[i] and not inc:
                return False
            else:
                curr = A[i]
        return True
                
            