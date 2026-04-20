class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # To include the current choice
            subset.append(nums[i])
            dfs(i+1)

            # Not to include the current choice
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res