class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []

        while r < len(nums):
            window = nums[l:r + 1]
            max_num = max(window)
            res.append(max_num)
            l += 1
            r += 1

        return res