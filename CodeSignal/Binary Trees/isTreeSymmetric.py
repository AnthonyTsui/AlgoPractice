# Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

# Example

# For

# t = {
#     "value": 1,
#     "left": {
#         "value": 2,
#         "left": {
#             "value": 3,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 4,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": 2,
#         "left": {
#             "value": 4,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 3,
#             "left": null,
#             "right": null
#         }
#     }
# }
# the output should be isTreeSymmetric(t) = true.

#Approach: At the root we want to check if the root is None and then compare the left and right nodes,
#from there, we know that the left most node needs to be compared with the right most node,
#and the second left-most node needs to be compared with the second right most node.
#

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    if not t: return True
    compareNodes = [(t.left, t.right)]
    while compareNodes:
        currNode = compareNodes.pop()
        leftNode, rightNode = currNode[0], currNode[1]
        if leftNode is None and rightNode is None:
            continue
        if not leftNode or not rightNode: return False
        if leftNode.value != rightNode.value: return False
        compareNodes.append((leftNode.left, rightNode.right))
        compareNodes.append((leftNode.right, rightNode.left))
    return True
