# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists( self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # Starting point 
        tail = dummy # Last node 

        # Compare nodes until one list runs out 
        while list1 and list2:
            if list1.val < list2.val: # Take smaller value to keep merged list sorted 
                tail.next = list1 # Move list1 forward
                list1 = list1.next
            else:
                tail.next = list2 # Move list2 forward 
                list2 = list2.next
            tail = tail.next # Move tail to added node 

        # one list is empty
        # attach sorted list to remaining list that is already sorted
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
