class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            # To include the choice
            subset.append(nums[i])
            dfs(i + 1, subset)

            # Not to include the choice and don't consider the duplicates
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, subset)

        dfs(0, [])
        return res
            