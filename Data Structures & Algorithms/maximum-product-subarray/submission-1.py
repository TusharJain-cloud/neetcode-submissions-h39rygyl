class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = 1, 1
        res = max(nums)

        for n in nums:
            # if n == 0:
                # cur_max, cur_min = 1, 1
                # continue

            tmp = n * cur_max
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            res = max(res, cur_max)


        return res
        