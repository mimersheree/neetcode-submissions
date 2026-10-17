class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        # Avoid more work and infinite recursion
        if original == color:
            return image
        
        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            # Stop if out of bounds or pixel is not original color
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or 
                image[r][c] != original):
                return
            
            # Recolor this pixel to mark it as visited
            image[r][c] = color

            # Explore up, down, left, right
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        dfs(sr, sc)
        return image 
