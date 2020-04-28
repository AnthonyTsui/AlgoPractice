# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".


#Approach: Utilize a stack, pop when we see '#'

#Time complexitiy: O(N + M) where N, M == len(S), len(T)
#Space complexity: O(N + M)
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS, stackT = [], []
        
        for s in S:
            if s == '#':
                if len(stackS): stackS.pop()
            else:
                stackS.append(s)
        
        for t in T:
            if t == '#':
                if len(stackT): stackT.pop()
            else:
                stackT.append(t)
        return stackS == stackT

