# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Approach: Go as far as possible into every left subtree,then append the parent node and then the right subtree

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack = []
        curr = root
        while stack or curr is not None:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        return output
        
        #Recursive approach
        # def traverse(node, output):
        #     if node is None:
        #         return
        #     traverse(node.left, output)
        #     output.append(node.val)
        #     traverse(node.right, output)
        # traverse(root, output)
        # return output