class CountSquares:

    def __init__(self):
        self.countPts = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.countPts[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.pts:
            if(abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            res += self.countPts[(x, py)] * self.countPts[(px, y)]
        
        return res
