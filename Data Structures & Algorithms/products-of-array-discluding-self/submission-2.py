class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res[i] will contain 
        # product of everything LEFT x product of everything RIGHT
        res = [1] * (len(nums))

        # FIRST PASS: Left -> Right
        # Store the product of all elements BEFORE i  
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # SECOND PASS: Right -> left 
        # Multiply res[i] by th eproduct of all elements AFTER i 
        postfix = 1 
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        # time: O(n)
        # space: O(1) extra space, O(n) space for output array