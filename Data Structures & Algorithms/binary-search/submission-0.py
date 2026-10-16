class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set search boundaries to the first and last indices
        l, r = 0, len(nums) - 1 

        # Continue while the search range is not empty 
        while l <= r: 
            # Find the middle index without adding l + r directly
            m = l + ((r - l) // 2)

            if nums[m] > target:
                # Target is smaler, search the left half
                r = m - 1 
            elif nums[m] < target:
                # Target is larger, search the right hhalf
                l = m + 1
            else: 
                # Target found, return index 
                return m 
        
        # Target is not in the array 
        return -1
