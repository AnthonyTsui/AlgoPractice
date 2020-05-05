# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

 

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
 

# Constraints:

# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5
# Accepted


#Approach:Scan from right to left to maintain the rightmost max element at i-th element
#Time Complexity: O(N)
#Space Complexity: O(N)

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        currMax = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], currMax = currMax, max(currMax, arr[i])
        return arr
        
        
        # mapping = {}
        # currMax = -1
        # for i in reversed(range(len(arr))):
        #     mapping[i] = currMax
        #     currMax = max(currMax, arr[i])
        # return mapping.values()
            
            