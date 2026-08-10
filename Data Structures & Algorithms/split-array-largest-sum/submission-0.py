class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        while l < r:
            mid = l + (r - l) // 2

            subarrays = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > mid:
                    subarrays += 1
                    curr_sum = num
                else:
                    curr_sum += num

            if subarrays > k:
                l = mid + 1
            else:
                r = mid

        return l