class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        t = 0
        rows, cols = len(grid), len(grid[0])

        min_heap = [[grid[0][0], 0, 0]]
        visit = set((0, 0))
        directions = [[0,1], [1, 0], [-1, 0], [0, -1]]

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            
            if r == rows - 1 and c == cols - 1:
                return t


            for row, col in directions:
                nei_r, nei_c = row + r, col + c
                
                if nei_r < 0 or nei_c < 0 or nei_r >= rows or nei_c >= cols or (nei_r, nei_c) in visit:
                    continue
                visit.add((nei_r, nei_c))
                heapq.heappush(min_heap, [max(t, grid[nei_r][nei_c]), nei_r, nei_c])

