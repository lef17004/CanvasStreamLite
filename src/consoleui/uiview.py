from .uigizmo import UiGizmo
from .uiinput import UiInput, InputType
from .uicanvasinterface import UiCanvasInterface

class UiView:
    def __init__(self):
        self.gizmos = []
        self.canvas = None

    def add_gizmo(self, gizmo: UiGizmo):
        self.gizmos.append(gizmo)

    def remove_gizmo(self, gizmo: UiGizmo):
        self.gizmos.remove(gizmo)

    def advance(self, input: UiInput):
        self.handle_input(input)
        self._draw()

    def register_to_manager(self, canvas: UiCanvasInterface):
        self.canvas = canvas

    def _draw(self):
        for gizmo in self.gizmos:
            gizmo.draw(self.canvas)

    def handle_input(self, input: UiInput):
        complete = False
        for gizmo in self.gizmos:
            if input.type == InputType.CLICK and gizmo.within_bounds(input.x, input.y):
                complete = gizmo.handle_input(input)

        return complete
