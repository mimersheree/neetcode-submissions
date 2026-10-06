class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):

            # Check only numbers after 1 
            for j in range(i + 1, len(nums)):

                # Check if pair adds up to target
                if nums[i] + nums[j] == target: 

                    # Return indices of the two numbers
                    return [i, j]
        return [] # Return empty if no valid pair exists