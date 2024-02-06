from random import randint
from quadtree import Quadtree


multiplicator: int = 2
WIDTH: int = 1280 * multiplicator
HEIGHT: int = 640 * multiplicator

qtree = Quadtree(-WIDTH / 2, -HEIGHT / 2,  WIDTH / 2, HEIGHT / 2)


for i in range(500):
    x = randint(int(-WIDTH / 2), int(WIDTH / 2))
    y = randint(int(-HEIGHT / 2), int(HEIGHT / 2))
    qtree.insert(x, y)


points = qtree.queryRactangle(10.0, 124.3, 100)
print(points)
