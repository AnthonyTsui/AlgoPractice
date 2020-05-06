# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

# If there are no nodes with an even-valued grandparent, return 0.

 

# Example 1:



# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

# Constraints:

# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.



#Approach: We utilize DFS that passes in the grandparent and parent of the current node we are at.
#Check the grandparent and parent, as well as as grandparent.val is even and add the current node val to self.answer if so.

#Time Complexity: O(N) where N = number of nodes 
#Space Complexity: O(height) of the tree 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.answer = 0
    
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node, parent, grandparent):
            if not node: return
            if parent and grandparent and grandparent.val%2 == 0:
                self.answer += node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
        
        dfs(root, None, None)
        return self.answer
            
        
        
        
#         def checkGrandchildren(node):
#             if not node.left and not node.right:
#                 return 0
#             grandchildren = []
#             answer = 0
#             if node.left: 
#                 grandchildren.append(node.left.left)
#                 grandchildren.append(node.left.right)
#             if node.right:
#                 grandchildren.append(node.right.left)
#                 grandchildren.append(node.right.right)
#             while grandchildren:
#                 curr = grandchildren.pop()
#                 if not curr:
#                     continue
#                 answer += curr.val
#             return answer
            
        
#         answer = 0
#         stack = [root]
#         while stack:
#             curr = stack.pop()
#             if not curr:
#                 continue
#             if curr.val % 2 == 0:
#                 answer += checkGrandchildren(curr)
#             stack.append(curr.left)
#             stack.append(curr.right)
#         return answer 