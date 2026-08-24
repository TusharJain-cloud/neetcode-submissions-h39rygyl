class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod = 1, 1
        res = nums[0]

        for n in nums:
            if n == 0:
                max_prod, min_prod = 1, 1
                # continue
            
            tmp = max_prod
            max_prod = max(max_prod * n, min_prod * n, n)
            min_prod = min(tmp * n, min_prod * n, n)
            res = max(res, max_prod)

        return res