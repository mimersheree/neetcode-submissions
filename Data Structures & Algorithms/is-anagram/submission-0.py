class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        # Hash maps store each character's frequency
        countS, countT = {}, {}

        # Count occurrences of each character in both strings  
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # If any character frequencies differ, they aren't anagrams
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        # All character frequencies match 
        return True 

