from .uiview import UiView
from .uicanvasinterface import UiCanvasInterface
from .uiinput import UiInput

class UiViewManager:
    def __init__(self, root: UiView, canvas: UiCanvasInterface):
        root.register_to_manager(canvas)
        self.view_stack = [root]
        self.canvas = canvas

    def stack_view(self, view: UiView):
        self.view_stack.append(view)

    def pop_view(self):
        self.view_stack.pop()

    def advance(self, input: UiInput):
        self.view_stack[0].advance(input)

        