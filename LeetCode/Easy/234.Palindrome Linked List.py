# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#One approach is to traverse the linked list and store our values into a list, and then check the list using left and right indexes to see if the list is a palindrome
#The other approach is to use two pointers, one slow that moves one node at a time, and one fast that moves two nodes at a time.
#We then traverse the node based on fast.next.next and check that we are able to move 2 nodes at once. As we traverse we save our current node into our reversed list variable,
#append our previous reversed list to it, then move slow up once.

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rList = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            #rList, rList.next, slow = slow, rList, slow.next
            temp = rList
            rList = slow
            slow = slow.next
            rList.next =temp
            
        if fast:
            slow = slow.next
        while rList and rList.val == slow.val:
            slow = slow.next
            rList = rList.next
        return not rList
        # toList = []
        # curr = head
        # while curr is not None:
        #     toList.append(curr.val)
        #     curr = curr.next
        # left, right = 0, len(toList)-1
        # while left < right:
        #     if toList[left] != toList[right]:
        #         return False
        #     left+= 1
        #     right -= 1
        # return True