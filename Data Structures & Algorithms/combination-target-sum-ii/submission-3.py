class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Need to sort, so we dont add duplicates
        
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i == len(candidates):
                return
            
            # To include the choice
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            
            # Not to include the choice
            cur.pop()
            # Now if we have same element that we previosly selected we should not consider it
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res