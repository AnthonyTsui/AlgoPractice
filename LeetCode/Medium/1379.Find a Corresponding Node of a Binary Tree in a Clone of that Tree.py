# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

# Follow up: Solve the problem if repeated values on the tree are allowed.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Time Complexity: O(N), potentially O(N + P) where P = path to target, but it could be at furthest right node anyway.
#Space Complexity: O(H), where H = height of the original binary tree 

#We traverse the entire original tree (potentially) to find target, and save our path to a list [path]. We then traverse the cloned 
#tree using the path in order to get to our target node.


class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        #Follow-up
        path = []
        def dfs(node):
            if not node:
                return False
            if node is target:
                return True
            if dfs(node.left):
                path.append(True)
                return True
            if dfs(node.right):
                path.append(False)
                return True
            return False
        dfs(original)
        
        for direction in reversed(path):
            if direction:
                cloned = cloned.left
            else:
                cloned = cloned.right
        return cloned
                
        
        # stack = [cloned]
        # while stack:
        #     curr = stack.pop()
        #     if not curr: continue
        #     if curr.val == target.val:
        #         return curr
        #     stack.append(curr.left)
        #     stack.append(curr.right)
        # return original