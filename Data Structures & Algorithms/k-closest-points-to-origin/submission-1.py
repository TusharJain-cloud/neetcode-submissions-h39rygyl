class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
            x, y = point
            dist = math.sqrt((0 - x)**2 + (0 - y)**2)
            heapq.heappush(min_heap, (dist, x, y))

        
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            res.append([x,y])
            k-=1

        return res
        