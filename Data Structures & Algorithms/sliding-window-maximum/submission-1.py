class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(K^(N - K))
        # l, r = 0, k - 1
        # res = []

        # while r < len(nums):
        #     window = nums[l:r + 1]
        #     max_num = max(window)
        #     res.append(max_num)
        #     l += 1
        #     r += 1

        # return res

        # Monotonically Decreasing Queue -> Deque
        q = collections.deque()
        res = []

        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val if we slide the window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res

        