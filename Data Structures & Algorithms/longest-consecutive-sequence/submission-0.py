class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # Set allows O(1) avg lookup
        longest = 0 

        for n in nums: 
            # Only start counting if n is the beginning of a sequence
            if (n - 1) not in numSet:
                length = 0

                # Count consecutive numbers starting from n 
                while (n + length) in numSet:
                    length += 1

                # Update the longest sequence found 
                longest = max(length, longest)
        return longest 