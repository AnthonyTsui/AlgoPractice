# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

#Time Complexity: O(a + b) 
#Space Complexity: O(1)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        numa, numb = 0, 0
        lena ,lenb = len(a)-1, len(b)-1
        for i in range(lena, -1, -1):
            numa += int(a[i])*(2**(lena-i))
        for i in range(lenb, -1, -1):
            numb += int(b[i])*(2**(lenb-i))
        return bin(numa + numb)[2:]