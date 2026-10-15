# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: an empty tree has depth of 0
        if not root:
            return 0

        # Recursively find the deeper subtree and add 1 to the current node
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

