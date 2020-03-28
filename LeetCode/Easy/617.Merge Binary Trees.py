# Given two binary trees and imagine that when you put one of them to cover the other, 
# some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. 
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of new tree.


#Approach: Create a new binary tree using a recursive helper function  to check both left and right of our current node positiosn
#Iterative approach using a stack of tuples to iterate through tress:
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        stack = [(t1,t2)]
        while len(stack):
            curr = stack.pop()
            if(curr[0] == None or curr[1] == None):
                continue
            curr[0].val += curr[1].val
            if(curr[0].left == None):
                curr[0].left = curr[1].left
            else:
                stack.append((curr[0].left, curr[1].left))
            if(curr[0].right == None):
                curr[0].right = curr[1].right
            else:
                stack.append((curr[0].right, curr[1].right))
        return t1


#I have no idea how I didnt think of this first, still a recursive solution
#Time complexity: 71.06% , 5.55%
# class Solution(object):
#     def mergeTrees(self, t1, t2):
#         """
#         :type t1: TreeNode
#         :type t2: TreeNode
#         :rtype: TreeNode
#         """
#         if not t1:
#             return t2
#         if not t2:
#             return t1
#         t1.val += t2.val
#         t1.left = self.mergeTrees(t1.left, t2.left)
#         t1.right = self.mergeTrees(t1.right, t2.right)
#         return t1

#Time: 88.65% time and 5.55% space
#Don't like this approach due to awful code readability 
# class Solution(object):
#     def mergeTrees(self, t1, t2):
#         """
#         :type t1: TreeNode
#         :type t2: TreeNode
#         :rtype: TreeNode
#         """
#         if t1 is None and t2 is None:
#             return None
#         if t1 is None:
#             return t2
#         if t2 is None:
#             return t1
#         newHead = TreeNode(t1.val + t2.val)
#         self.mergeHelper(newHead, t1, t2)
#         return newHead
        
#     def mergeHelper(self, node, t1, t2):
#         if t1.left is None and t2.left is None:
#             node.left = None
#         if t1.left is None:
#             node.left = t2.left
#         elif t2.left is None:
#             node.left = t1.left
#         else:
#             node.left = TreeNode(t2.left.val + t1.left.val)
#             self.mergeHelper(node.left, t1.left, t2.left)
#         if t2.right is None and t2.right is None:
#             node.right = None
#         if t1.right is None:
#             node.right = t2.right
#         elif t2.right is None:
#             node.right= t1.right
#         else:
#             node.right = TreeNode(t1.right.val + t2.right.val)
#             self.mergeHelper(node.right, t1.right, t2.right)