#Given an integer array arr, count element x such that x + 1 is also in arr.

#If there're duplicates in arr, count them seperately.class Solution(object):

# Example 1:

# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
# Example 2:

# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
# Example 3:

# Input: arr = [1,3,2,3,5,0]
# Output: 3
# Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
# Example 4:

# Input: arr = [1,1,2,2]
# Output: 2
# Explanation: Two 1s are counted cause 2 is in arr.


#Approach: For each x in arr: we need to check if x+1 is in array.
#We can save all the unique values in a set() which will also provide look up time of O(1)
#We can the iterate through the original array again and check if x+1 is in our set

#TGime complexity: O(N), creating set(arr) takes O(N) and looping through the original array again or N size is O(N)

#Space Complexity: O(N)

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        uniqueVals = set(arr)
        
        answer = 0
        
        for elem in arr:
            if elem+1 in uniqueVals:
                answer += 1
        
        return answer
        
        