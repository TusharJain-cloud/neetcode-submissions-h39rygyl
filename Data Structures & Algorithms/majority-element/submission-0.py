class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyers Moore's Algorithm Optimized --> T.C = O(n) & S.C = O(1)
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n

            count += (1 if res == n else -1)

        return res

        # Hashmap solution: T.C = O(n) & S.C = O(n)
        # res, max_count = 0, 0
        # count = {}

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     res = n if count[n] > max_count else max_count
        #     max_count = max(count[n], max_count)
        
        # return res