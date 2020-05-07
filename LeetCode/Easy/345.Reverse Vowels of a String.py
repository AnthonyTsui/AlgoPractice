# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"
# Example 2:

# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".

#Time complexity: O(N)
#Space Complexity: O(N) as we are storing the string as list, (since strings are immutable in python)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(list('aeiouAEIOU'))
        s = list(s)
        
        left,right = 0, len(s)-1
        
        while left < right:
            while s[left] not in vowels and left < right:
                left += 1
            while s[right] not in vowels and left <right:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)
        
        
#         vowels = {'e' ,'i', 'o', 'u', 'a', 'A', 'I', 'E', 'O', 'U'}
        
#         stack = []
        
#         for i in range(len(s)):
#             if s[i] in vowels:
#                 stack.append(s[i])
        
#         if not len(stack): return s
        
#         answer = ''
        
#         for i in range(len(s)):
#             if s[i] in vowels:
#                 answer += stack.pop()
#             else:
#                 answer += s[i]
#         return answer
        