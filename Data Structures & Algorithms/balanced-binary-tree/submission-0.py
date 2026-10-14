# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Base case: empty subtree is balanced with height 0 
        def dfs(root): 
            if not root: return [True, 0]

            # Recursively check left and right subtrees (postorder DFS)
            left, right = dfs(root.left), dfs(root.right)

            # Current node is balaneced if both subtrees are balanced
            # and their heights differ at most by 1 
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # Return balance status and current subtree height
            return [balanced, 1 + max(left[1], right[1])]

        # The first value tells whether the entire tree is balanced 
        return dfs(root)[0]