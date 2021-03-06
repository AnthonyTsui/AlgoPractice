# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 

# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
 

# Constraints:

# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6



#Approach:Utilize a dictionary to record every seen differences and their possible combinations.
#Use sort() on the arr before hand, as this means every element's adjacent elements will be as close to its own value as possible.

#Time complexity: O(nlogn)
#Space complexity: O(N)

import collections

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        if not len(arr): return []
        
        distances = collections.defaultdict(list)
        sortedArr = sorted(arr)
        for i in range(0, len(arr)-1):
            diff = abs(sortedArr[i] - sortedArr[i+1])
            distances[diff].append([sortedArr[i],sortedArr[i+1]])
        
        minDistance = min(distances.keys())
        return distances[minDistance]