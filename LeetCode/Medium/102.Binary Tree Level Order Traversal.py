# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

#Approach: We utilize a stack to keep track of all the nodes in our current level, as well as to order the nodes in each level from left to right
#Our stack starts as [root], and for each element in our current stack we pop() the element and append its value to currLevel[], as well as check if it has 
#left and right children. We append these children if they exist. Everytime we pop an element we check to see if the stack is now empty (meaning we have gone through all elements
#current level) We then set stack = nextStack to begin traverseing the next level, making sure to also set nextStack and currLevel for an empty list in preparation for 
#our next level in our traversal

#Time complexity: O(N) as we traverse through all N nodes in the tree
#Space complexity: At most our stack will hold all the leaf nodes of the tree (as this is the level with the most possible nodes in a full binary tree)
#Which is roughly ~(N/2), so our worst space complexity during run time is O(N) 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        if not root:
            return output
        stack = [root]
        nextStack, currLevel = [], []
        while stack:
            currNode = stack.pop(0)
            currLevel.append(currNode.val)
            
            if currNode.left: nextStack.append(currNode.left)
            if currNode.right: nextStack.append(currNode.right)
            if not stack:
                stack = nextStack
                nextStack = []
                output.append(currLevel)
                currLevel = []
        return output
            
            