class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(n)
        res = 0
        cur_sum = 0
        prefix_sum = { 0 : 1 }

        for n in nums:
            cur_sum += n
            diff = cur_sum - k

            res += prefix_sum.get(diff, 0)

            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0) 

        return res
        
        # O(n^2)
        # res = 0

        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i, len(nums)):
        #         cur_sum += nums[j]

        #         if cur_sum == k:
        #             res += 1

        # return res

        
        # O(n^3)
        # res = 0

        # for i in range(len(nums)):

        #     for j in range(i, len(nums)):
                
        #         if sum(nums[i:j + 1]) == k:
        #             res += 1

        # return res