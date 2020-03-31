# Write a program to find the node at which the intersection of two singly linked lists begins.

# For example, the following two linked lists:


# begin to intersect at node c1.

 

# Example 1:


# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. 
# From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


#Approaches: iterate through both list to get the depth, then iterate together to the first same corresponding node
#Other approach: iterate through both list and check if the nodes are the same, on first pass if not set them to the other linked list and iterate through the 
#argument itself which will terminate if  no intersection.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None: 
            return None
        
        pointerA = headA
        pointerB = headB
        
        while pointerA !=  pointerB:
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next
            
        return pointerA

        
        # depthA, depthB = 0, 0
        # currA, currB = headA, headB
        # while currA:
        #     depthA += 1
        #     currA = currA.next
        # while currB:
        #     depthB += 1
        #     currB = currB.next
        # currA, currB = headA, headB
        # while depthA > depthB:
        #     currA = currA.next
        #     depthA -= 1
        # while depthB > depthA:
        #     currB = currB.next
        #     depthB -= 1
        # while currA and currB:
        #     if currA == currB:
        #         return currA
        #     currA = currA.next
        #     currB = currB.next
        # return None