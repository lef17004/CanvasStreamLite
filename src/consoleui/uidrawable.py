from .uicanvasinterface import UiCanvasInterface
from .uigeometry import UiGeometry
from .uiorigin import UiOrigin
from .uivector import UiSize, UiCoord
from .uichar import UiChar

class UiDrawable:
    def __init__(self):
        self.geometry = UiGeometry()
        self._data = [
            [UiChar('')]
        ]

    def draw(self, canvas: UiCanvasInterface):
        ...

    @property
    def origin(self):
        return self.geometry.origin
    
    @origin.setter
    def origin(self, value: UiOrigin):
        self.geometry.origin = value

    @property
    def size(self):
        return self.geometry.size
    
    @size.setter
    def size(self, value: UiSize):
        self.geometry.size = value

    @property
    def position(self):
        return self.geometry.position
    
    @position.setter
    def position(self, value: UiCoord):
        self.geometry.position = value