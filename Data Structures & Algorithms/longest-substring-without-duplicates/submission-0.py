class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Track unique characters in window 
        charSet = set()
        l = 0
        res = 0

        # Expand window, if duplicate -> shrink from left 
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            # Add current character 
            charSet.add(s[r])
            
            # Update max window length
            res = max(res, r - l + 1)
        return res 
