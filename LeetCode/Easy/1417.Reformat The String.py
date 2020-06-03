# Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

# Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

# Example 1:

# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
# Example 2:

# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by digits.
# Example 3:

# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by characters.
# Example 4:

# Input: s = "covid2019"
# Output: "c2o0v1i9d"
# Example 5:

# Input: s = "ab123"
# Output: "1a2b3"

#Approach: iterate through the initial string, seperating the characters based on isalpha() or not 
#If the number of digits vs number of letters is greater than 1, then we know that a valid permutation is not possible
#From there, set the larger stack to firstStack, and the other to secondStack
#We then continue to pop and add the chars from both stacks and append them to our answer, at the end we check to see if we have a letter remaining from firstStack

#Time Complexity: O(N) where N = len(s)
#Space Complexity :O(N) since we are storing all the characters from the initial string

class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        numStack, charStack = [], []
        for c in s:
            if c.isalpha():
                charStack.append(c)
            else:
                numStack.append(c)
        if abs(len(numStack) - len(charStack)) > 1:
            return ''
        
        if len(numStack) > len(charStack):
            firstStack, secondStack = numStack, charStack
        else:
            firstStack, secondStack = charStack, numStack
            
        ans = ''
        
        while firstStack and secondStack:
            first, second = firstStack.pop(), secondStack.pop()
            ans += first + second
        if firstStack:
            ans += firstStack.pop()
        return ans