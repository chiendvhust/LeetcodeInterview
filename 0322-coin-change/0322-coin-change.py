class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp(amount) is the fewest number of coins that you need to make up that amount
        @lru_cache(None)
        def dp(amount):
            if amount == 0:
                return 0
            res = math.inf
            for coin in coins:
                if amount >= coin:
                    res = min(res, dp(amount - coin) + 1)
            return res
        res = dp(amount)
        if res == math.inf:
            res = -1
        return res