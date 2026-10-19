class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        # Reverse strings to process bits from right to left
        a, b = a[::-1], b[::-1]

        # Process each bit up to the length of the longer string
        for i in range(max(len(a), len(b))):
            # Get the current bit, or 0 if this string has no bit here
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            # Add both bits and carry from the previous position
            total = digitA + digitB + carry

            # The remainder gives the curreny binary bit
            char = str(total % 2)
            res = char + res

            # Integer division gives the carry for the next position
            carry = total // 2

        # Add any remaining carry as leftmost bit
        if carry:
            res = "1" + res
        return res
            

