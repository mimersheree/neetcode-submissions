# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists( self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node makes it easy to build result 
        dummy = ListNode() 
        tail = dummy  

        # Compare current nodes from both sorted lists 
        while list1 and list2:
            if list1.val < list2.val: # Take smaller value to keep merged list sorted 
                tail.next = list1 # Move list1 forward
                list1 = list1.next
            else:
                tail.next = list2 # Move list2 forward 
                list2 = list2.next
            tail = tail.next # Move result forward 

        # One list is empty -> attach the remaining sorted nodes
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next # Skip dummy node
