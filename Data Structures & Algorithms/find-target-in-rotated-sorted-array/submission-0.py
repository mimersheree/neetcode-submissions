class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        while l <= r:
            mid = (l + r) // 2

            # Target found 
            if target == nums[mid]:
                return mid

            # Left half is sorted 
            if nums[l] <= nums[mid]:

                # Target is outside the sorted left half; search right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 
                else:
                    # Target is within the sorted left half 
                    r = mid - 1 
            
            # Right half is sorted 
            else: 

                # Target is outside the sorted right half; search left 
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    # Target is within the sorted right half
                    l = mid + 1 
        return -1
                