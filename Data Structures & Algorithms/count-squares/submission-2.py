class CountSquares:

    def __init__(self):
        self.pts = defaultdict(int)
        self.pts_list = []

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1
        self.pts_list.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0

        for x, y in self.pts_list:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            
            res += self.pts[(px, y)] * self.pts[(x, py)]
        
        return res
