class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        # prefix & suffix (optimal)

        prefix = 1 # first pass (left to right)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1 # second pass (right to left)
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        # time: O(n), space: O(1) extra space, O(n) space for output array