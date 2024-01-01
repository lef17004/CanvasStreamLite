from .uibox import UiBox
from .uitext import UiText
from .uivector import UiCoord, UiSize
from .uicanvasinterface import UiCanvasInterface
from .uiorigin import UiOrigin
from .uigizmo import UiGizmo
from .uiaction import UiAction
from .uiinput import UiInput, InputType

class UiButton(UiGizmo):
    def __init__(self):
        super().__init__()
        self.place_at(UiCoord(0, 0), UiOrigin.TOP_LEFT)
        self.set_size(UiSize(20, 5))
        self.box = UiBox(UiCoord(0, 0), UiSize(20, 5))
        self.text = UiText("Press")
        # self.text.place_at(UiCoord(10, 3), UiOrigin.CENTER)
        self.text.connect_to(self.box, UiOrigin.CENTER, UiOrigin.CENTER)
        self.action: UiAction = None

    def draw(self, canvas: UiCanvasInterface):
        self.box.draw(canvas)
        self.text.draw(canvas)

    def onclick(self):
        pass

    def handle_input(self, input: UiInput) -> bool:
        if input.type == InputType.CLICK and self.action:
            self.action.execute()
            return True
        return False