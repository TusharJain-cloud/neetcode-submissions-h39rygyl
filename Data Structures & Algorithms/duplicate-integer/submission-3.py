class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}

        for n in nums:
            if n in dup:
                return True
            dup[n] = 1
        
        return False
        
        