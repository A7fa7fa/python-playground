from typing import Any, List
from queryMode import QueryMode
from Quadtree.point import Point
from segment import Segment

class Quadtree():

    def __init__(self, minX: float, minY: float, maxX: float, maxY: float) -> None:
        self.min = Point(min(minX, maxX), min(minY, maxY),)
        self.max = Point(max(minX, maxX), max(minY, maxY),)
        self.center = Point((self.max.x + self.min.x) / 2, (self.max.y + self.min.y) / 2)

        self.data = Segment(self.center.x, self.center.y, self.width / 2, self.height / 2)
        self.allDataRef: List[Point] = []

    @property
    def width(self) -> float:
        return self.max.x - self.min.x

    @property
    def height(self) -> float:
        return self.max.y - self.min.y

    def insert(self, x: float | int, y: float | int, userDate: Any | None = None) -> None:
        if (x < self.min.x or x > self.max.x or y < self.min.y or y > self.max.y):
            raise ValueError(f"Out of bound. min{self.min}:max{self.max}")
        pos = Point(x, y, userDate)
        self.data.insert(pos)
        self.allDataRef.append(pos)

    def queryRactangle(self, centerX: float, centerY: float, radius: float) -> List[Point]:
        return self.data.query(centerX, centerY, radius, mode = QueryMode.rectangle)

    def queryCircle(self, centerX: float, centerY: float, radius: float) -> List[Point]:
        return self.data.query(centerX, centerY, radius, mode =  QueryMode.circle)

    def getAll(self) -> List[Point]:
        return self.allDataRef