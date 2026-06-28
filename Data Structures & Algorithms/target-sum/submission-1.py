class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp = defaultdict(int)
        # dp[0] = 1

        # for i in range(len(nums)):
        #     next_dp = defaultdict(int)
        #     for cur_sum, count in dp.items():
        #         next_dp[cur_sum + nums[i]] += count 
        #         next_dp[cur_sum - nums[i]] += count 
        #     dp = next_dp
        
        # return dp[target]
        dp = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])

            return dp[(i, total)]

        return backtrack(0,0)