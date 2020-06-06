# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

# Example 1:

# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
# Example 2:

# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
# Example 3:

# Input: s = "bcbcbc"
# Output: 6



class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        vowels = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        d = {0:-1}
        state = ans = 0
        
        for i, c in enumerate(s):
            if c in vowels:
                state ^= vowels[c]
            if state not in d:
                d[state] = i
            else:
                ans = max(ans, i - d[state])
        return ans
        