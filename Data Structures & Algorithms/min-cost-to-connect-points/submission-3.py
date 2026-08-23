class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj_list = {i : [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj_list[i].append([dist, j])
                adj_list[j].append([dist, i])


        min_heap = [[0, 0]]
        visit = set()

        cost = 0

        while len(visit) < n:
            dist, point = heapq.heappop(min_heap)
            if point in visit:
                continue
            
            visit.add(point)
            cost += dist
            for dist2, point2 in adj_list[point]:
                if point2 not in visit:
                    heapq.heappush(min_heap, [dist2, point2])

        return cost
