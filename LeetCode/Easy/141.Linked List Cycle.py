# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.


# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


#Approach: If the value are distinct we can save all the values we've seen into a dictionary and then 
#check each node we traverse if it is in our dictionary, however this is O(N) space, as we store all the nodes
#Second approach for us would be to use a faster and slow pointer and see if they ever overlap. 
#In the case that there is no cycle, we run the risk of trying to get .next of NoneType, so wrap in an exception

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(head == None or head.next == None):return False
        fast, slow = head.next, head
        while fast != slow:
            if (fast == None or slow == None): return False
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return False
        return True
            