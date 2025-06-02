class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
      
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # No coins needed to make 0 amount

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]