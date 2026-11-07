from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        total = 0

        for (x, y), freq in self.points.items():

            if x != qx and abs(x - qx) == abs(qy - y):

                point1 = (x, qy)
                point2 = (qx, y)

                total += (
                    freq
                    * self.points.get(point1, 0)
                    * self.points.get(point2, 0)
                )

        return total