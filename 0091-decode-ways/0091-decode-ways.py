class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp(i) is number ways to decode message s[i...n-1]
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 1
            
            res = 0
            if s[i] != '0':
                res += dp(i + 1)
            if i + 1 < n and (s[i] == '1' or s[i] == '2' and s[i + 1] <= '6'):
                res += dp(i + 2)
            return res
        return dp(0)