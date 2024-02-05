# Follow: How to install p5 https://p5.readthedocs.io/en/latest/install.html


from typing import List
import p5
from p5.core.constants import CENTER

from quadtree import Quadtree
from Quadtree.point import Point

def drawParticles(pos: List[Point], fill: bool = False) -> None:
    p5.stroke_weight(1)
    p5.stroke(100)
    p5.no_fill()

    if fill:
        p5.fill(255, 0, 0)

    for p in pos:
        p5.ellipse(p.x, p.y, 10, 10)

def drawRect(x: float, y: float, r: float) -> None:
    p5.stroke_weight(1)
    p5.stroke(0,0,255)
    p5.no_fill()
    p5.rect(x, y, r * 2, r * 2, mode = CENTER)

mult = 1
WIDTH = 1280 * mult
HEIGHT = 640 * mult

qtree = Quadtree(-WIDTH/ 2, -HEIGHT/ 2,  WIDTH/ 2, HEIGHT/ 2)

for i in range(50):
    x = p5.random_uniform(-WIDTH/ 2, WIDTH / 2)
    y = p5.random_uniform(-HEIGHT/ 2, HEIGHT /2)
    qtree.insert(x, y)

def setup() -> None:
    p5.size(WIDTH, HEIGHT)
    p5.translate(WIDTH / 2, HEIGHT / 2)
    p5.background(0,0,0)
    p5.no_fill()
    p5.stroke_weight(2)
    p5.stroke(255)


def draw() -> None:
    p5.translate(WIDTH / 2, HEIGHT / 2)
    p5.background(0,0,0)

    allParticles = qtree.getAll()

    drawParticles(allParticles)

    x: float = mouse_x - WIDTH / 2
    y: float = mouse_y - HEIGHT / 2
    r: int = 100

    drawRect(x, y, r)

    points = qtree.queryRactangle(x, y, r)

    drawParticles(points, True)

    if mouse_is_pressed:
        print('clicked')
        # add 5 points to tree
        for _ in range(5):
            x = p5.random_uniform(-30, 30) - (WIDTH / 2)
            y = p5.random_uniform(-30, 30)- (HEIGHT /2)
            qtree.insert(mouse_x + x, mouse_y + y)


if __name__ == '__main__':
    p5.run()
