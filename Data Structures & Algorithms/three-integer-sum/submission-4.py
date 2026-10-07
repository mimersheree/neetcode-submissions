class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Sort array to use two pointers and skip duplicates 
        nums.sort() 

        # Fix the first number, then use two pointers 
        # to find the other two numbers 
        for i, a in enumerate(nums):

            # Since array is sorted, if a > 0,
            # the other numbers will be > 0 and can't add up to 0
            if a > 0:
                break
            
            # Skip duplicate values for the first number 
            # to avoid duplicate triplets 
            if i > 0 and a == nums[i - 1]:
                continue

            # Two pointers search for remaining 2 numbers 
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                # Sum is too large -> move right pointer left 
                if threeSum > 0:
                    r -= 1
                
                # Sum is too small -> move left pointer right 
                elif threeSum < 0:
                    l += 1
                
                # Found valid triplet 
                else:
                    res.append([a, nums[l], nums[r]])

                    # Move both pointers to search for another 
                    l += 1
                    r -= 1

                    # Skip duplicate left values 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res