# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

# We repeatedly make duplicate removals on S until we no longer can.

# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

# Example 1:

# Input: "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 

# Note:

# 1 <= S.length <= 20000
# S consists only of English lowercase letters.


#Approach: Utilize a stack to pop() adjacent (previous) letters if the current letter is the same as the one on the top of the stack.
#Time complexity: O(N) where N = len(S)
#Space Complexity: O(N) 


class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        tempStack = []
        for s in S:
            if not len(tempStack) or tempStack[-1] != s:
                tempStack.append(s)
            else:
                tempStack.pop()
        return ''.join(tempStack)