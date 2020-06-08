# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# Example 1:

# Input: "III"
# Output: 3
# Example 2:

# Input: "IV"
# Output: 4

#Time Complexity :O(N)
#Space Complexity:O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        if not len(s): return 0
        vals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        ans = 0
        
        for i in range(len(s)):
            if i == len(s)-1 or vals[s[i]] >= vals[s[i+1]]:
                ans += vals[s[i]]
            else:
                ans -= vals[s[i]]
        return ans 
#         if len(s) == 1: 
#             return vals[s[0]]
        
#         curr, ans = 0, 0
#         while curr < len(s):
#             if curr == len(s)-1:
#                 ans += vals[s[curr]]
#                 break
#             x, y = vals[s[curr]], vals[s[curr+1]]
#             if y > x:
#                 ans += y - x
#                 curr += 2
#             else:
#                 ans += x
#                 curr += 1
#         return ans