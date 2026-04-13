class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # This is the brute force approach just to implement things in T.C -> O(n)
        # for n in range(len(nums)):
        #     if nums[n] == target:
        #         return n

        # return -1

        # Now, the optimal solution -> Binary Search -> T.C: O(log(n))
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1