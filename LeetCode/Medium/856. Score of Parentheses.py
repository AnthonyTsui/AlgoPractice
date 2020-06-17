# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: "()"
# Output: 1
# Example 2:

# Input: "(())"
# Output: 2
# Example 3:

# Input: "()()"
# Output: 2
# Example 4:

# Input: "(()(()))"
# Output: 6


# Input: "(()(()))"
# "(    ()   (()) )"
# () (())
# ()  2*1 + 1 = 3 *2 == 6

#Parse through  the string: We know s[0] == (
#We can establish it as left = 1, right = 0
#While left != right: keep traversing through the string, this will be the interior of our current parenthnesis
#Example: ( ()(()) )
#We can return: 2*scoreOfParenthesis(interior) + whatever else is in the string

#Using a stack:
#Maintain a stack and traverse the string.
#If the char == '(' we append to stack, and if ')' we know we just exited a depth, so pop and adjust the score
#based on max(2*pop(), 1))

#Time Complexity: O(N) where N = len(S) for stack, N^2 for recursive method
#Space Complexity: O(N) 
    
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for s in S:
            if s == '(':
                stack.append(0)
                continue
            if s == ')':
                p = stack.pop()
                stack[-1] += max(p*2, 1)
        return stack[-1]
        
        
        # if not S: return 0
        # if S == '()': return 1
        # left, right, inside = 0, 0, ''
        # for i in range(len(S)):
        #     s = S[i]
        #     if s == '(': left += 1
        #     if s == ')': right += 1
        #     inside = inside + s
        #     if left == right:
        #         if inside != '()':
        #             return (2*self.scoreOfParentheses(inside[1:-1])) + self.scoreOfParentheses(S[i+1:])
        #         else:
        #             return 1 + self.scoreOfParentheses(S[i+1:])
        
        