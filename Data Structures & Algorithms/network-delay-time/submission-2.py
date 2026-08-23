class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i : [] for i in range(1, n + 1)}

        for s, d, cost in times:
            adj_list[s].append([d, cost])
        
        min_heap = [[0, k]]
        visit = set()
        t = 0

        while min_heap:
            cost, d = heapq.heappop(min_heap)

            if d in visit:
                continue

            visit.add(d)
            t = cost

            for nei, nei_cost in adj_list[d]:
                if nei not in visit:
                    heapq.heappush(min_heap, [nei_cost + cost, nei])
            
        return t if len(visit) == n else -1