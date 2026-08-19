class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recurs(steps):
            if steps <= 2:
                return steps

            if steps in memo:
                return memo[steps]

            memo[steps] = recurs(steps - 1) + recurs(steps - 2)
            return memo[steps]
        return recurs(n)


        