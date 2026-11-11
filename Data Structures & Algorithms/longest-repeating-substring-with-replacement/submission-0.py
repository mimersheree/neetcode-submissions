class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0

        for r in range(len(s)):
            # Expand window and count the new character
            count[s[r]] = 1 + count.get(s[r], 0)

            # Track the highest character frequency in the window
            maxf = max(maxf, count[s[r]])

            # Shrink window if replacements needed exceed k
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # Update the longest valid window 
            res = max(res, r - l + 1)

        return res 