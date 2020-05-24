# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Note:

# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
# Example 1:

# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


# import operator

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                if token == '+':
                    stack[-2] = stack[-2] + stack[-1]
                elif token == '-': 
                    stack[-2] = stack[-2] - stack[-1]
                elif token == '*':
                    stack[-2] = stack[-2] * stack[-1]
                else:
                    stack[-2] = int(float(stack[-2]) / stack[-1])
                stack.pop()
            else:
                stack.append(int(token))
        return stack[0]

#         if not len(tokens): return 0
        
#         nums = []
#         # operations = {
#         #     '+': operator.add,
#         #     '-':operator.sub,
#         #     '*':operator.mul,
#         #     '/':operator.div,
#         # }
#         for token in tokens:
#             if token.isdigit() or token.lstrip('-').isdigit():
#                 nums.append(int(token))
#                 continue
#             right, left = nums.pop(), nums.pop()
#             if token == '+':
#                 nums.append(right + left)
#             elif token == '-':
#                 nums.append(left-right)
#             elif token == '*':
#                 nums.append(left*right)
#             else:
#                 nums.append(int(float(left)/right))
        
#         return nums.pop()