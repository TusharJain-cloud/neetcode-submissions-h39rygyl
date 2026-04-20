class Solution:
    def hammingWeight(self, n: int) -> int:
        # Solution 1 --> O(32)
        # res = 0

        # while n:
        #     res += n % 2
        #     n = n >> 1
        
        # return res

        # Solution 2 --> O(1)
        res = 0

        while n:
            n &= (n-1)
            res += 1
        
        return res
        