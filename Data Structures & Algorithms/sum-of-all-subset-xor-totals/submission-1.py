class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # Backtracking: O(2 ^ n)
        # def backtrack(i, total):
        #     if i >= len(nums):
        #         return total

            
        #     return backtrack(i + 1, total ^ nums[i]) + backtrack(i + 1, total)
            
        # return backtrack(0, 0)

        # Combinatronics: O(n)

        res = 0

        for n in nums:
            res = res | n

        return res * 2 ** (len(nums) - 1)