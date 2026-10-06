class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Two pointers: compare characters from both ends
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric characters 
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            # If opp. characters, not a palindrome
            if s[l].lower() != s[r].lower():
                return False

            # Move both pointers inward
            l, r = l + 1, r - 1
        return True

    # Check if character is a letter or number
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))