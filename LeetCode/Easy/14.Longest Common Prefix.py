# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs: return ''
        ans = ''
        sortedWords = sorted(strs, key= len)
        ans = sortedWords[0]
        for word in sortedWords:
            prefixLength = len(ans)
            while ans != word[:prefixLength]:
                ans = ans[:-1]
                prefixLength = len(ans)
                if not prefixLength:
                    return ''
        return ans