# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        output = []
        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[:len(p)-1])
        i = len(p)-1
        while i < len(s):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                output.append(i - len(p) + 1)
            sCounter[s[i-len(p)+1]] -= 1
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]
            i += 1;
        return output
    
        
        
        #Bad time complexity: O(s * pLogp)
#         output = []
#         seenAnagrams = set()
#         sortedSubstring = ''.join(sorted(p))
#         for i in range(0, len(s)-len(p)+1):
#             if s[i:i+len(p)] in seenAnagrams:
#                 output.append(i)
#                 continue
#             currSubstring = ''.join(sorted(s[i:i+len(p)]))
#             if currSubstring == sortedSubstring:
#                 output.append(i)
#                 seenAnagrams.add(s[i:i+len(p)])
#         return output
        