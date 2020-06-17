# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

# Return that integer.

 

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
 

# Constraints:

# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5

#Time Complexity: O(N)
#SPace Complexity :O(1)

from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        goal = len(arr)//4
        for i in range(len(arr)):
            if arr[i] == arr[i+goal]: return arr[i]
        # curr, currLength = arr[0], 1
        # for i in range(1, len(arr)):
        #     if arr[i] != curr:
        #         curr, currLength = arr[i], 1
        #         continue
        #     currLength += 1
        #     if currLength > goal: return curr
        # return arr[0]