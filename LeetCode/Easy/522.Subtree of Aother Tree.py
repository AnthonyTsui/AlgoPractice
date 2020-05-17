# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
 

# Example 2:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.

#Time Complexity: O(S*T)
#Space Complexity: O(S)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        
        def checkTree(a, b):
            if not a and not b:
                return True
            elif a and not b or b and not a:
                return False
            
            if a.val != b.val:
                return False
            
            return checkTree(a.left, b.left) and checkTree(a.right, b.right)
        
        def dfs(a, b):
            if not a:
                return False
            if a.val == b.val and checkTree(a, b):
                return True
            return dfs(a.left, b) or dfs(a.right, b)
        
        return dfs(s, t)