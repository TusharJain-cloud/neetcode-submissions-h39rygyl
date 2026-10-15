class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adj, visit, path, order):
            if src in path:
                return False
            if src in visit:
                return True

            visit.add(src)
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei, adj, visit, path, order):
                    return False
            
            path.remove(src)
            order.append(src)
            return True


        def top_sort(edges):
            adj = defaultdict(list)

            for e1, e2 in edges:
                adj[e1].append(e2)
            
            visit = set()
            path = set()
            order = []
            for src in range(1, k + 1):
                if not dfs(src, adj, visit, path, order):
                    return []

            return order[::-1]


        row_order = top_sort(rowConditions)
        col_order = top_sort(colConditions)
        if not row_order or not col_order:
            return []

        val_to_row = { n : i for i, n in enumerate(row_order)}
        val_to_col = { n : i for i, n in enumerate(col_order)}

        res = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            r, c = val_to_row[num], val_to_col[num]
            res[r][c] = num

        return res