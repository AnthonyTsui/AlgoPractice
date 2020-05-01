# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

 

# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.
# Example 4:

# Input: arr = [5]
# Output: -1
# Example 5:

# Input: arr = [7,7,7,7,7,7,7]
# Output: 7

#Approach:Use a dictionary in order to store every number and its frequency as we traverse through the array initially
#We then traverse through the dictionary itself to check if it is a lucky number, and set the answer to the max(num, answer)

#Time complexity: O(N) 
#Space complexity: O(N)

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}
        answer = -1
        for num in arr:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        for num, val in freq.items():
            if val == num:
                answer = max(num, answer)
        return answer