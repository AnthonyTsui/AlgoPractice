# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

# Return the largest string X such that X divides str1 and X divides str2.

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Note:

# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] and str2[i] are English uppercase letters.

#Time Complexity: O(N^2)
#Space Complexity :O(1)

import re

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        def gcd(a, b):
            return b if a == 0 else gcd(b%a, a)
        length = gcd(len(str1), len(str2))
        substr = str2[:length]
        regex = '(' + str2[:length] + ')+'
        return substr if re.fullmatch(regex, str1) and re.fullmatch(regex, str2) else ''

        # s1, s2 = len(str1), len(str2)
        # if s2 > s1:
        #     return self.gcdOfStrings(str2, str1)
        # if str1[:len(str2)] == str2:
        #     if len(str1) == len(str2):
        #         return str2
        #     return self.gcdOfStrings(str1[len(str2):], str2)
        # return ''