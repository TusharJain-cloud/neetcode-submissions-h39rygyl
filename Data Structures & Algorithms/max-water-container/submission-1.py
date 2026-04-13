class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute Force --> T.C: O(n^2)
        # res = 0

        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         area = (j - i) * min(heights[i], heights[j])
        #         res = max(res, area)
        
        # return res

        # Optimal solution: 2 Pointers: T.C -> O(n)
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res