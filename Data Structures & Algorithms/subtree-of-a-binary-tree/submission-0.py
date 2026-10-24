# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s = TreeNode, t = TreeNode) -> bool:
        # Base case: an empty tree is always a subtree
        if not t: 
            return True

        # A non-empty subtree cannot exist inside an empty tree
        if not s:
            return False 

        # Check whether the trees match exactly at current node
        if self.sameTree(s, t):
            return True

        # If not, search the left or right subtree
        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))
    
    def sameTree(self, s, t):
        # Both nodes are empty, so this part of the tree matches 
        if not s and not t:
            return True
        
        # If both nodes exist and values match, compare both subtrees
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        
        # One node is missing or values differ, so trees do not match
        return False 