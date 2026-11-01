class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BRUTE FORCE 
        # res = 0 

        # for l in range(len(height):
        #   for r in range(l + 1, len(height)):
        #       area = (r - l) * (min(height[l], height[r]))
        #       res = max(res, area)
        # return res 

        # Linear time solution: O(n)
        # Start at both ends 
        res = 0 
        l, r = 0, len(heights) - 1 


        # Width x shorter height 
        while l < r:
            area = (r - l) * min(heights[l], heights[r])

            # Track maximum area 
            res = max(res, area)

            # Move the shorter point inward 
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1 
        return res 