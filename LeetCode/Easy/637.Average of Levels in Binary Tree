# Question:

# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.


#use a stack to handle all the nodes of the current level of the tree, pop them and get the average before adding all the children of each one again

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        stack = [root]
        answer = []
        while stack:
            currMax = 0
            currCount = 0
            nextStack = []
            while len(stack):
                currNode = stack.pop()
                currMax += currNode.val
                currCount += 1
                if currNode.left: nextStack.append(currNode.left)
                if currNode.right: nextStack.append(currNode.right)
            stack = nextStack
            answer.append(float(currMax)/float(currCount))
        return answer
            
#92.09% speed, 16.67% space
            