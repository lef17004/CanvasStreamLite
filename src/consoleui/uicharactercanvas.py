from .uichar import UiChar
from .uivector import UiVector

class UiCharacterCanvas:
    def __init__(self, width: int, height: int) -> None:
        self._data = [UiChar('') for i in range(width * height)]
        self._has_changed: bool = False
        self._chached_string: str = ""
        self._width = width
        self._height = height

    def draw_char(self, char, x: int, y: int):
        self._has_changed = True
        index = self._calc_index(x, y)
        self._data[index] = char

    def _calc_index(self, x, y):
        return (y * self._width) + x

    

    