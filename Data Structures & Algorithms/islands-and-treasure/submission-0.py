class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def addRooms(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols or (r,c) in visit or grid[r][c] == -1):
                return 
            visit.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist
                addRooms(r + 1,c)
                addRooms(r - 1,c)
                addRooms(r,c + 1)
                addRooms(r,c - 1)
            dist += 1

        