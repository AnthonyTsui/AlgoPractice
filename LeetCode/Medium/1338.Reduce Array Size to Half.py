# Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

# Return the minimum size of the set so that at least half of the integers of the array are removed.

 

# Example 1:

# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
# Example 2:

# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the new array empty.
# Example 3:

# Input: arr = [1,9]
# Output: 1
# Example 4:

# Input: arr = [1000,1000,3,7]
# Output: 1
# Example 5:

# Input: arr = [1,2,3,4,5,6,7,8,9,10]
# Output: 5


#Time Complexity: O(nlogn)
#Space Complexity: O(N)
import collections

class Solution:
    def minSetSize(self, arr):
        ans, toHalf = 0, 0
        
        for i, freq in enumerate(sorted(collections.Counter(arr).items(), key=lambda x: x[1], reverse = True)):
            ans += 1
            toHalf += freq
            if toHalf >= len(arr)//2:
                return i + 1
        return ans
        
        
#         freq = collections.Counter()
#         for num in arr:
#             freq[num] += 1
        
#         toHalf = len(arr)//2 
#         if len(arr) % 2 == 1: toHalf += 1
#         ans = 0
#         for num, f in sorted(freq.items(), key = lambda x : x[1], reverse = True):
#             ans += 1
#             toHalf -= f
#             if toHalf <= 0:
#                 break
#         return ans
            
    
        
        