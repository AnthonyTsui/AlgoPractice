# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

#Time Complexity: O(N)
#Space Complexity: O(N) where n = len(digits)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
 
        
        if not len(digits): return []
        
        depth, answer = len(digits)-1, 0
        
        for d in digits:
            answer += d*(10**depth)
            depth -= 1
        
        return [int(i) for i in str(answer+1)]
        
        
#         carry = False
        
#         digits[-1] += 1
        
#         if digits[-1] == 10:
#             carry = True
#             digits[-1] = 0
        
#         for i in range(len(digits)-2, -1, -1):
#             if not carry:
#                 break
#             if digits[i] == 9 and carry:
#                 digits[i] = 0
#                 carry = True
#             else:
#                 digits[i] += 1
#                 carry = False
        
#         if carry:
#             digits.insert(0, 1)
#             return digits
        
#         return digits