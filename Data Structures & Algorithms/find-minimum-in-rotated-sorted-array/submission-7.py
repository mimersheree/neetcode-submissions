class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l < r:
            # Current range is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2

            # Track the smallest value found
            res = min(res, nums[m])

            # Left half is sorted; search right
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                # Keep mid because it could be the minimum
                r = m

        return min(res, nums[l])