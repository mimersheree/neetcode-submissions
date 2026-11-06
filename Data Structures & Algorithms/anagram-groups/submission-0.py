class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         res = defaultdict(list) # Mapping charCount to list of anagrams 

         for s in strs:
            count = [0] * 26 # Create a frequency array for letters a ... z 

            # Count occurrences of each character 
            for c in s:
                count[ord(c) - ord("a")] += 1 

            # Use tuple as hashable key and group matching anagrams 
            res[tuple(count)].append(s)
        
        # Return all grouped anagrams 
         return list(res.values())