from .uichar import UiChar
from .uiorigin import UiOrigin
from .uicanvasinterface import UiCanvasInterface
from .uivector import UiCoord, UiSize
from .uidrawable import UiDrawable
from .uigizmo import UiGizmo

class UiText(UiGizmo):
    def __init__(self, value: str):
        super().__init__()
        self._data = []

        for char in value:
            self._data.append(UiChar(char))

        self.set_size(UiSize(len(self._data), 1))

    def draw(self, canvas: UiCanvasInterface):
        for i, char in enumerate(self._data):
            canvas.draw_char(char, int(self.get_position().x + i), int(self.get_position().y))