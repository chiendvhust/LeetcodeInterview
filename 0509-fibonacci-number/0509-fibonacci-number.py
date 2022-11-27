class Solution:
    memo = {}
    def fib(self, n: int) -> int:
        if n <= 1: return n
        if n in Solution.memo: return Solution.memo[n]
        
        Solution.memo[n] = self.fib(n-1) + self.fib(n-2)
        return Solution.memo[n]