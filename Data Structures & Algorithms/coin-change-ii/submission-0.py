class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # OPTIMIZED: O(N*A)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
        
        return dp[amount]
        
        # Recursive: O(N * M)
        # cache = {}

        # def dfs(i, a):
        #     if a == amount:
        #         return 1
        #     if a > amount:
        #         return 0
        #     if i >= len(coins):
        #         return 0
        #     if (i, a) in cache:
        #         return cache[(i, a)]
            
        #     cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)

        #     return cache[(i, a)]
        
        # return dfs(0, 0)