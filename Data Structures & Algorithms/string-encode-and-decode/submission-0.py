class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        # Encode each string as: length + delimiter + string 
        for s in strs:
            res  += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # Tracks the start of each encoded string 

        while i < len(s):
            j = i

            # Find the delimiter separating length from the string 
            while s[j] != "#":
                j += 1
            
            # Read the length of the original string 
            length = int(s[i:j])

            # Extract exactcly length characters after the delimiter 
            res.append(s[j + 1 : j + 1 + length])

            # Move i to the beginning of the next encoded string 
            i = j + 1 + length
            
        return res 

        
