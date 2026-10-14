# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Track the longest diameter found
        self.res = 0 
        
        # DFS returns the height of each subtree 
        def dfs(curr):
            if not curr:
                return 0  # Base case: Empty subtree has height 0 

            # Get the heights of the left and right subtrees 
            left = dfs(curr.left)
            right = dfs(curr.right)

            # Longest path through this node = left height + right height 
            self.res = max(self.res, left + right)    

            # Return height to the parent node  
            return 1 + max(left, right)
        
        dfs(root)
        return self.res # Diameter is measured in edges 

