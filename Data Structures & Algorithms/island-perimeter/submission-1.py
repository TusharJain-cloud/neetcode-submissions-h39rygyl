class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # base case 1: if the given cell is out of bounds or the cell next to cell of value 1(land) is value 0(water) then add 1 to the perimeter 
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1
            
            # base case 2: if the given cell is already visited then we don't add anything
            if (r, c) in visit:
                return 0

            # now run dfs in all 4 directions
            visit.add((r, c))
            perimeter = dfs(r, c + 1)
            perimeter += dfs(r, c - 1)
            perimeter += dfs(r + 1, c)
            perimeter += dfs(r - 1, c)
            return perimeter
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r, c)

        # T.C & O.C --> O(N*M) where N is number of rows and M is number of columns

