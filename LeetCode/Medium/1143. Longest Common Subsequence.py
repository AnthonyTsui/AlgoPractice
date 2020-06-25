# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

# If there is no common subsequence, return 0.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

#Time Complexity: O(N*M) where N = len(text1), M = len(text2)
#Space Complexity: O(N*M)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text2 == text1: return len(text1)
        ans = [[0]*(len(text2)+1) for i in range(len(text1)+1)]

        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    ans[i+1][j+1] = ans[i][j] + 1
                else:
                    ans[i+1][j+1] = max(ans[i+1][j], ans[i][j+1])
        return ans[-1][-1]
    

