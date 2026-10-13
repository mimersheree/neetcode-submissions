class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0 

        # Every second occurrence completes a pair
        # Each pair adds 2 characters to the palindrome 
        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2
        
        # A palindrome can have at most one-odd count character
        # Use one leftover character as the center, if avaiable c
        for cnt in count.values():
            if cnt % 2:
                res += 1
                break
        
        # Return total characters used in pairs and optional center
        return res 