class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            e = (l + r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/e)
            
            if hours <= h:
                res = min(res, e)
                r = e - 1
            else:
                l = e + 1
        
        return res