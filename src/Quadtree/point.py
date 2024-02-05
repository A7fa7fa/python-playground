from typing import Any

class Point():
    def __init__(self, x: float, y: float, userData: Any | None = None) -> None:
        self.x = x
        self.y = y
        self.userData = userData

    def __str__(self) -> str:
        return f"x:{self.x} y:{self.y}"
