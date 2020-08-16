# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


class Solution:

    #This solution is much faster, checking string equality is O(1). And slicing is only K where K = len(s) that we are slicing
    #So still O(N^2) as we are iterating through S in a for loop, and for each element we are slicing at most a K len string where K can be len(s)-1
    def longestPalindrome(self, s: str) -> str:
        start = 0 
        maxlen = 1
        for i in range(len(s)):
            if i - maxlen >= 1 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
                start = i - maxlen - 1 
                maxlen += 2
                continue
            if i - maxlen >= 0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
                start = i - maxlen 
                maxlen += 1
        return s[start:start+maxlen]
        
        
#         l, r = 0 ,0
#         currmax = ''
#         def expand(s, left, right):
#             r, l = right, left
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 r +=1 
#                 l -= 1
#             return s[l+1:r] #No longer a palindrome, so return the last substring
        
#         for i in range(len(s)):
#             currlen = expand(s, i, i)
#             if len(currlen) > len(currmax):
#                 currmax = currlen
#             currlen = expand(s, i, i+1)
#             if len(currlen) > len(currmax):
#                 currmax = currlen

#         return currmax
            
        
            