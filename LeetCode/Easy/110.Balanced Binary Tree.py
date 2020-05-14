# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

# Example 1:

# Given the following tree [3,9,20,null,null,15,7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:

# Given the following tree [1,2,2,3,3,null,null,4,4]:

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4



#Time Complexity: O(N)
#Space Complexity: O(h) where h = height of the tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkDepth(node):
            if not node:
                return 0
            left = checkDepth(node.left)
            right = checkDepth(node.right)
            if left == -1 or right == -1 or abs(left -right) > 1:
                return -1
            return 1 + max(left, right)
            
        balanced = checkDepth(root)
        
        return balanced != -1 
            
            