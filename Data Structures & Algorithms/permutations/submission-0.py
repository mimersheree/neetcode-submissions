class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case: an empty list has one permutation-the empty list
        if len(nums) == 0:
            return [[]]

        # Recursively generate permutations of the lis without the first number
        perms = self.permute(nums[1:])
        res = []

        # Insert the first number into every possible position
        # of each smaller permutation 
        for p in perms:
            for i in range(len(p) + 1):
                # Copy the permutation so existing results are not modified
                p_copy = p.copy()

                # Insert the first number at the current position
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        # Return all generated permutations
        return res