# Given an n-ary tree, return the postorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

# Follow up:

# Recursive solution is trivial, could you do it iteratively?

 

# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
        def postorder(self, root):
            """
            :type root: Node
            :rtype: List[int]
            """
            output = []
            if not root: return output
            stack = [root]
            
            while stack:
                curr = stack.pop()
                output.append(curr.val)
                stack.extend(curr.children)
            return output[::-1]
    
    
    #Recursive
#     def postorder(self, root):
#         """
#         :type root: Node
#         :rtype: List[int]
#         """
#         output = []
#         self.potraversal(root, output)
#         return output
#     def potraversal(self, root, output):
#         if not root: return
#         for child in root.children:
#             self.potraversal(child, output)
#         output.append(root.val)
        