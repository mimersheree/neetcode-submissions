class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26

        # Count available characters in magazine
        for c in magazine:
            count[ord(c) - ord('a')] += 1

        # Use one available character for each needed character
        for c in ransomNote:
            count[ord(c) - ord('a')] -= 1
            if count[ord(c) - ord('a')] < 0:
                return False      # If count is negative, return false
        
        return True