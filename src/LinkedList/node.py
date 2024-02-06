class Node():

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node | None = None
