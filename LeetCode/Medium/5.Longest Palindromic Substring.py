# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        currmax = ''
        def expand(s, left, right):
            r, l = right, left
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r +=1 
                l -= 1
            return s[l+1:r] #No longer a palindrome, so return the last substring
        
        for i in range(len(s)):
            currlen = expand(s, i, i)
            if len(currlen) > len(currmax):
                currmax = currlen
            currlen = expand(s, i, i+1)
            if len(currlen) > len(currmax):
                currmax = currlen
        return currmax
            
        