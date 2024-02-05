from typing import List
from queryMode import QueryMode

from point import Point

class Segment():

    def __init__(self, centerX: float, centerY: float, halfWidth: float, halfHeight: float) -> None:
        self.center = Point(centerX, centerY)
        self.halfWidth = halfWidth
        self.halfHeight = halfHeight

        self.southWest: Segment | None = None
        self.southEast: Segment | None = None
        self.northWest: Segment | None = None
        self.northEast: Segment | None = None

        self.capacity = 4
        self.data: List[Point] = []

    def insert(self, pos: Point) -> bool:
        if not self.__isInside(pos.x, pos.y):
            return False

        hasChildren = self.southEast is not None and self.southWest is not None and self.northEast is not None and self.northWest is not None
        if hasChildren:
            return self.__insertIntoChildren(pos)

        hasCapacity = len(self.data) < self.capacity
        if hasCapacity:
            self.data.append(pos)
            return True

        self.__createChilds()
        return self.__insertIntoChildren(pos)


    def query(self, x: float, y: float, r: float, mode: QueryMode = QueryMode.rectangle) -> List[Point]:
        """returns list of intersected Position"""
        if mode == QueryMode.circle:
            raise NotImplementedError("Mode query by circle is not implemented")

        foundPos: List[Point] = []
        if not self.__intersectsRectangle(x, y, r):
            return foundPos

        if self.southWest:
            foundPos += self.southWest.query(x, y, r, mode = mode)
        if self.southEast:
            foundPos += self.southEast.query(x, y, r, mode = mode)
        if self.northWest:
            foundPos += self.northWest.query(x, y, r, mode = mode)
        if self.northEast:
            foundPos += self.northEast.query(x, y, r, mode = mode)

        foundPos += self.__pointInsideRectangle(x, y, r)

        return foundPos

    def __insertIntoChildren(self, pos: Point) -> bool:
        if self.southWest and self.southWest.insert(pos):
            return True
        if self.southEast and self.southEast.insert(pos):
            return True
        if self.northWest and self.northWest.insert(pos):
            return True
        if self.northEast and self.northEast.insert(pos):
            return True
        raise ValueError("Can not insert in any Segment")


    def __isInside(self, x: float, y: float) -> bool:
        """favours East Segment if x position of point is on x boundary.\n
        favours south Segment if y position of point is on y boundary"""
        return (x >= (self.center.x - (self.halfWidth)) <= x < (self.center.x + (self.halfWidth))
            and y >= (self.center.y - (self.halfHeight)) <= y < (self.center.y + (self.halfHeight)))

    def __createChilds(self) -> None:
        childSegmentWidth = self.halfWidth / 2
        childSegmentHeight = self.halfHeight / 2
        self.southWest = Segment(self.center.x - childSegmentWidth,
                                self.center.y - childSegmentHeight,
                                childSegmentWidth,
                                childSegmentHeight)
        self.southEast = Segment(self.center.x + childSegmentWidth,
                                self.center.y - childSegmentHeight,
                                childSegmentWidth,
                                childSegmentHeight)
        self.northWest = Segment(self.center.x - childSegmentWidth,
                                self.center.y + childSegmentHeight,
                                childSegmentWidth,
                                childSegmentHeight)
        self.northEast = Segment(self.center.x + childSegmentWidth,
                                self.center.y + childSegmentHeight,
                                childSegmentWidth,
                                childSegmentHeight)

    def __intersectsRectangle(self, x: float, y: float, r: float) -> bool:
        if self.__isInside(x, y):
            return True

        isRecOutsideOfSegment = ((self.center.x + self.halfWidth <= x - r)
                                or (self.center.x  - self.halfWidth >= x + r)
                                or (self.center.y + self.halfHeight <= y - r)
                                or self.center.y - self.halfHeight >= y + r)
        if isRecOutsideOfSegment:
            return False

        return True

    def __pointInsideRectangle(self, x: float, y: float, r: float) -> List[Point]:
        """returns points which are inside of rectangle"""
        foundPos: List[Point] = []
        for p in self.data:
            insideRectangle = (p.x >= (x - (r))
            and p.x <= (x + (r))
            and p.y >= (y - (r))
            and p.y <= (y + (r)))
            if  insideRectangle:
                foundPos.append(p)

        return foundPos