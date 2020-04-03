# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:

# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
 

# Example 2:

# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #Go through potential "middle" of a palindrome of the string,
        #and expand outwards in order to find all palindromes that with this midpoint
        # ans = 0
        # n = len(s)
        # for i in range((2*n)-1):
        #     left = i / 2
        #     right = left + i%2
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         ans += 1
        #         left -= 1
        #         right += 1
        # return ans
    
        #Another potential solution is to utilize dynamic programming to get the palindrome substrings
        #Both approaches will run in n^2 time
        answer = 0
        n = len(s)
        palindromes = [[0]*n for c in s]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i + 1) < 3 or palindromes[i+1][j-1] == 1):
                    palindromes[i][j] = 1
                    answer += 1
        #print(palindromes)
        return answer
