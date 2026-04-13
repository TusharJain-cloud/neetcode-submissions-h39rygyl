class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashmap solution: T.C -> O(n) 
        duplicate = {}

        for n in nums:
            if n in duplicate:
                return True
            
            duplicate[n] = 1

        return False
        
        # O(n^2) Solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        
        # return False