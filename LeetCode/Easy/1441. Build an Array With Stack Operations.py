# Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

# Build the target array using the following operations:

# Push: Read a new element from the beginning list, and push it in the array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
# You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

# Return the operations to build the target array.

# You are guaranteed that the answer is unique.

#Time Complexity: O(N) where N = n 
#Space Complexity :O(N) 

from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        idx, res, length = 0, [], len(target)
        for num in range(1,n+1):
            if idx == length:
                return res
            res.append('Push')
            if num != target[idx]:
                res.append('Pop')
            else:
                idx += 1
        return res
        
        
        
#         index, ans = 0, []
        
#         for num in range(1,target[-1]+1):
#              if num in target:
#                 ans.append('Push')
#              else:
#                 ans.append('Push')
#                 ans.append('Pop')
#         return ans