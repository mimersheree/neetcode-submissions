class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Set stores numbers we've already seen 
        hashset = set()

        for n in nums:
            # Already seen -> duplicate found 
            if n in hashset:
                return True

            # First time seeing n -> remembers it 
            hashset.add(n)
        
        # No duplicate found 
        return False