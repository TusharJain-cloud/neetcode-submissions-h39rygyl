class CountSquares:

    def __init__(self):
        self.pts_count = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0

        for x, y in self.pts:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue

            res += self.pts_count[(x, py)] * self.pts_count[(px, y)]

        return res
