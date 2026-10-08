# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Slow moves 1 step; fast moves 2 steps
        slow, fast = head, head 

        # Continue while fast can move 2 steps
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next

            # If they meet, fast has caught slow -> cycle exists
            if slow == fast:
                return True
        
        # Fast reached the end -> no cycle
        return False 