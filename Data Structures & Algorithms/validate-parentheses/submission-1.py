class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        # Check if stack is not empty and top matches corresponding opening bracket
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # if yes, pop stack, otherwise, return false
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False