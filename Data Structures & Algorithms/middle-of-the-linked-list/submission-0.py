# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # Fast moves 2 steps, check that both steps are valid
        while fast and fast.next:
            slow = slow.next            # Move slow pointer 1
            fast = fast.next.next       # Move fast pointer 1 

        # When fast reaches the end, slow is at the middle
        # If the list has an even length, return the second middle 
        return slow 