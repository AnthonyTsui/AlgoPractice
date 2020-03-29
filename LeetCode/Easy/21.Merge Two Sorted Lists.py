# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


#First Approach: Create new linked list and iterate through the two input linked lists as we go, if one is greater than the other then just iterate one, else we iterate both

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#Another Iterative Solution 
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newHead = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return newHead.next


#Time complexity: O(N + M) where n & m are the lengths of l1 and l2, Space Complexity: O(M+N) since we are creating a new list that merges both linked lists

# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         newHead = ListNode(None)
#         curr = newHead
#         while l1 or l2:
#             if not l1:
#                 curr.next = l2
#                 break
#             if not l2:
#                 curr.next = l1
#                 break
#             v1, v2 = l1.val, l2.val
            
#             if v1 > v2:
#                 curr.next = ListNode(v2)
#                 curr = curr.next
#                 l2 = l2.next
#             elif v1 == v2:
#                 curr.next = ListNode(v1)
#                 curr.next.next = ListNode(v2)
#                 curr = curr.next.next
#                 l1 = l1.next
#                 l2 = l2.next
#             else:
#                 curr.next = ListNode(v1)
#                 curr = curr.next
#                 l1 = l1.next
            
#         return newHead.next