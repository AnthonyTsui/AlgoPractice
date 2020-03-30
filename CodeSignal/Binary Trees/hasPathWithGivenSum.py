
# Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    if not t: return False
    nodesToTraverse = [(t, 0)]
    while nodesToTraverse:
        currNode = nodesToTraverse.pop()
        node, currVal = currNode[0], currNode[1]
        currVal += node.value
        if currVal == s and not node.left and not node.right:
            return True
        if node.left: nodesToTraverse.append((node.left, currVal))
        if node.right: nodesToTraverse.append((node.right, currVal))
    return False
