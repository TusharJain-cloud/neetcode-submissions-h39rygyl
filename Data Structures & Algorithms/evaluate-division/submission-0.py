class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list) #{a : [b, a/b]

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q, visit = deque(), set()
            q.append([src, 1])

            while q:
                n, w = q.popleft()

                visit.add(n)
                if n == target:
                    return w

                for node, weight in adj[n]:
                    if node not in visit:
                        q.append([node, w * weight])
                        visit.add(node)
                    
            return -1
        
        return [ bfs(src, target) for src, target in queries ]