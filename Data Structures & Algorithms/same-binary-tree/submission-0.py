# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both nodes are empty, this part of the tree matches
        if not p and not q:
            return True

        # If only one node is empty or their values differ, trees are not the same 
        if not p or not q or p.val != q.val:
            return False 
        
        # Recursively compare corresponding left and right subtrees
        # Both must match for the trees to be identical 
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))