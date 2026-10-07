class Solution:
    def isValid(self, s: str) -> bool:
        # Stack stores opening brackets 
        # closeToOpen maps each closing bracket -> matching opening bracket
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:

            # Closing bracket -> check the most recent opening bracket 
            if c in closeToOpen:

                # Top of stack must match the closing bracket 
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # Match found -> remove opening bracket 
                else:
                    return False # Wrong match or nothing to match 
            else:
                # Opening bracket -> save it for later matching
                stack.append(c)
        
        # Valid only if every opening bracket is matched 
        return True if not stack else False