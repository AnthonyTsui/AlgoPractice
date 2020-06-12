# Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Return the power of the string.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
# Example 3:

# Input: s = "triplepillooooow"
# Output: 5
# Example 4:

# Input: s = "hooraaaaaaaaaaay"
# Output: 11
# Example 5:

# Input: s = "tourist"
# Output: 1

#Time Complexity :O(N)
#Space Complexity: O(1)

class Solution:
    def maxPower(self, s: str) -> int:
        maxLength = 1
        currLength = 1
        curr =  s[0]        
        for i in range(1, len(s)):
            if s[i] == curr:
                currLength += 1
            else:
                currLength = 1
                curr = s[i]
            maxLength = max(maxLength, currLength)
            # if maxLength < currLength:
            #     maxLength = currLength
        return maxLength
    
        
        
#         if not s: return 0
#         curr, maxLength = 1, 1 
        
#         for i,c in enumerate(s):
#             if i == 0: continue
#             print (i, c, curr, maxLength)
#             if c == s[i-1]:
#                 curr += 1
#                 if curr > maxLength:
#                     maxLength = curr
#             else:
#                 curr = 1
#         return maxLength
                