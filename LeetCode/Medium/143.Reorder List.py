# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


#Time Complexity: O(N)
#Space Complexity: O(1)
#This question can be seen as taking the second half of the linked list, reversing it, and then splicing the two halves together


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head: 
            return
        
        #Find midpoint:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        
        #Reverse second half
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next
            
        #Merge the two halves of the linked list
        first, second = head, pre
        while second.next:
            first.next , first = second, first.next
            second.next, second = first, second.next
        return head