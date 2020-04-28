# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Approach: use two pointers, one that traverses 2 nodes at a time while the other traverses one at a time. When the faster pointer
#reaches the end of the list, the slow pointer will only have traversed by half.

#Time complexity: O(N)
#Space complexity:O(1)

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        
        fast, slow = head.next, head
        
        while fast:
            if not fast.next:
                return slow.next
            fast = fast.next.next
            slow = slow.next
        
        return slow