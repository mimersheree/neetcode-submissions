class Solution:
    def majorityElement(self, nums):
        # res = current canditate 
        # count = candidate's vote count
        res = count = 0

        for num in nums:
            # No current candiate -> choose this number 
            if count == 0:
                res = num
            
            # Same number = +1 vote 
            # Different number = -1 vote 
            count += (1 if num == res else -1)
        return res