# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = reversed portion; curr = node being processed 
        prev, curr = None, head 

        while curr: 
            nxt = curr.next     # Save next node before breaking link
            curr.next = prev    # Reverse the pointer
            prev = curr         # Grow reversed portion 
            curr = nxt          # Move to next unprocessed node 

        # prev is the new head after curr reaches None 
        return prev 
