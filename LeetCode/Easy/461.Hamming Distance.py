# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        #Realize that 1010 vs 0001 has hamming distance of 3, and that if we xor 1010 0001 we can 1011
        #and counting the 1s will yield the result
        
        return bin(x^y).count('1')
        
        #Convert to binary numbers and check for differences
        # firstInt, secondInt = bin(x)[2:], bin(y)[2:]
        # firstLength= len(firstInt)-1
        # secondLength = len(secondInt)-1
        # output = 0
        # while firstLength >= 0 or secondLength >= 0:
        #     if firstLength >=0 and secondLength >=0:
        #         output += 1 if firstInt[firstLength] != secondInt[secondLength] else 0
        #         firstLength -= 1
        #         secondLength -= 1
        #     elif firstLength >=0:
        #         if firstInt[firstLength] == '1': 
        #             output += 1
        #         firstLength -= 1
        #     else:
        #         if secondInt[secondLength] == '1': 
        #             output += 1
        #         secondLength -= 1
        # return output
            