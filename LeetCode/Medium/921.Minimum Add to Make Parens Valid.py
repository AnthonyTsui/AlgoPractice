# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

#Time Complexity: O(N)
#Space Complexity: O(1)

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left, right = 0 ,0
        for s in S:
            if s == '(':
                left += 1
            else:
                if left:
                    left -= 1
                else:
                    right += 1
        return right + left
        # stack = []
        # for s in S:
        #     if s == '(':
        #         stack.append(s)
        #     else:
        #         if stack and stack[-1] == '(':
        #             stack.pop()
        #         else:
        #             stack.append(s)
        # return len(stack)