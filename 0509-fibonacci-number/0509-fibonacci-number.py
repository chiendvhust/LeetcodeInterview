class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp, dp1, dp2 = 0, 1, 0
        for i in range(2, n+1):
            dp = dp1 + dp2
            dp2 = dp1
            dp1 = dp
        return dp