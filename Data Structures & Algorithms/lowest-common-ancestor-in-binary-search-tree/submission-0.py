# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start at the root
        curr = root

        while curr:
            # If both targets are larger, search the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both targets are smaller, search the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # Targets split sides, or one equals curr; curr is thee LCA
                return curr