from consoleui import UiCanvasInterface
from consoleui import UiChar, UiCoord
from application.canvas import Canvas

WIDTH = 9.6015625
HEIGHT = 13

class ConsoleStreamCanvas(UiCanvasInterface):
    def __init__(self, canvas: Canvas, width: int, height: int) -> None:
        super().__init__(width, height)
        self.canvas = canvas

    def draw_char(self, char: UiChar, x: int, y: int):
        x_final = x * WIDTH
        y_final = y * HEIGHT
        # self.canvas.fill_style = 'red'
        # self.canvas.fill_rect(50, 50, 10, 20)
        self.canvas.set_text_align('center')
        self.canvas.set_text_baseline('middle')
        # self.canvas.fill_style = 'black'
        self.canvas.fill_text(char.character, x_final + (WIDTH / 2), y_final + (HEIGHT / 2))

    def draw_char_(self, char: UiChar, position: UiCoord):
        x = (position.x * WIDTH) + (WIDTH / 2)
        y = (position.y * HEIGHT) + (HEIGHT / 2)
        self.canvas.set_text_align('center')
        self.canvas.set_text_baseline('middle')
        self.canvas.fill_text(char.character, x, y)

    def clear():
        ...