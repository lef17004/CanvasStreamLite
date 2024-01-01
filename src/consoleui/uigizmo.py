from __future__ import annotations
from .uivector import UiSize, UiCoord
from .uiorigin import UiOrigin, calc_location
from .uicanvasinterface import UiCanvasInterface
from .uiinput import UiInput, InputType
from .uigeometry import UiGeometry

class UiGizmo:
    def __init__(self):
        self.geometry = UiGeometry()
        self.redraw = False
        self.resort = False
        self.is_visible = True
        self.z_index = 0
        self.tile = None

    def draw(self, canvas: UiCanvasInterface):
        pass

    def place_at(self, position: UiCoord, origin: UiOrigin):
        self.set_position(calc_location(position, origin, UiOrigin.TOP_LEFT, self.get_size()))

    def position_at(self, origin: UiOrigin):
        return calc_location(self.get_position(), UiOrigin.TOP_LEFT, origin, self.get_size())

    def connect_to(self, other_gizmo: UiGizmo, other_origin: UiOrigin, this_origin):
        other_location = other_gizmo.position_at(other_origin)
        self.place_at(other_location, this_origin)

    def handle_input(self, input: UiInput) -> bool:
        return False
    
    def within_bounds(self, x, y):
        return self.geometry.is_in_bounds(UiCoord(x, y))
    
    def get_position(self) -> UiCoord:
        return self.geometry.position
    
    def set_position(self, value: UiCoord):
        self.geometry.position = value

    def get_size(self) -> UiSize:
        return self.geometry.size
    
    def set_size(self, value: UiSize):
        self.geometry.size = value

