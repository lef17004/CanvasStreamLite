from .uichar import UiChar
from .uivector import UiCoord

class UiCanvasInterface:
    def __init__(self, width: int, height: int) -> None:
        ...

    def draw_char(self, char: UiChar, x: int, y: int):
        ...

    def draw_char_(self, char: UiChar, position: UiCoord):
        ...

    def clear():
        ...