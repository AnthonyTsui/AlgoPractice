# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

# direction can be 0 (for left shift) or 1 (for right shift). 
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.

 

# Example 1:

# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation: 
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"
# Example 2:

# Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
# Output: "efgabcd"
# Explanation:  
# [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
# [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
# [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
# [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"

#Time complexity: O(N): Where N is the number of elements in shift, as we iterate through them to find out our 
#Space Complexity: O(1): We only store shiftLeft and shiftRight amounts

class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        if not shift:
            return s
        
        shiftleft, shiftright = 0, 0
        for val in shift:
            if val[0] == 0:
                shiftleft += val[1]
            else:
                shiftright += val[1]
                
        
        shiftleft, shiftright = shiftleft%len(s), shiftright%len(s)

        shiftAmount = abs(shiftleft - shiftright)
       
        if shiftleft > shiftright:
            return s[shiftAmount:] + s[:shiftAmount]
        else:
            return s[len(s)-shiftAmount:] + s[:len(s)-shiftAmount]


