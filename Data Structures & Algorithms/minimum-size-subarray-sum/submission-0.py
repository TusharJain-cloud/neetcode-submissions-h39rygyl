class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, sum_of_window = float("inf"), 0

        l = 0

        for r in range(len(nums)):
            sum_of_window += nums[r]
            while sum_of_window >= target:
                res = min(res, r - l + 1)
                sum_of_window -= nums[l]
                l += 1
        

        return 0 if res == float("inf") else res