# Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


#Time Complexity: O(N) where N = number of nodes in tree
#Space Complexity: O(H) max stack is H where H = height of our tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    runningSum = 0
    def bstToGst(self, node):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if node.right: self.bstToGst(node.right)
        node.val = self.runningSum = self.runningSum + node.val
        if node.left: self.bstToGst(node.left)
        return node  
        
        # stack = []
        # curr = root
        # runningSum = 0 
        # while stack or curr:
        #     if curr:
        #         stack.append(curr)
        #         curr = curr.right
        #     else:
        #         curr = stack.pop()
        #         temp = curr.val
        #         curr.val += runningSum
        #         runningSum += temp
        #         curr = curr.left
        # return root
        
            
        
            
            
        