class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 way to climb 1 step or stay at the starting point
        one, two = 1, 1

        for i in range(n - 1):
            # Save the previous count before updating
            temp = one

            # Current ways = ways from 1 step below + 2 steps below
            one = one + two

            # Shift the previous count forward
            two = temp
        
        # Return the number of ways to reach step n
        return one 
            