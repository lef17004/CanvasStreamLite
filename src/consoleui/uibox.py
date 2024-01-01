from .uivector import UiCoord, UiSize
from .uiorigin import UiOrigin, calc_location, calc_location_with_offset
from .uichar import UiChar
from .uicharactercanvas import UiCharacterCanvas
from .uigizmo import UiGizmo
from .uitile import UiTile

LIGHT_HORIZONTAL = '─'
LIGHT_VERTICAL = '│'
LIGHT_TOP_LEFT = '┌'
LIGHT_TOP_RIGHT = '┐'
LIGHT_BOTTOM_LEFT = '└'
LIGHT_BOTTOM_RIGHT = '┘'

LIGHT_TOP_LEFT_CURVED = "╭"
LIGHT_TOP_RIGHT_CURVED = "╮"
LIGHT_BOTTOM_RIGHT_CURVED = "╯"
LIGHT_BUTTOM_LEFT_CURVED = "╰ "

# Heavy Box Drawing Characters
HEAVY_HORIZONTAL = '━'
HEAVY_VERTICAL = '┃'
HEAVY_TOP_LEFT = '┏'
HEAVY_TOP_RIGHT = '┓'
HEAVY_BOTTOM_LEFT = '┗'
HEAVY_BOTTOM_RIGHT = '┛'

# Double Box Drawing Characters
DOUBLE_HORIZONTAL = '═'
DOUBLE_VERTICAL = '║'
DOUBLE_TOP_LEFT = '╔'
DOUBLE_TOP_RIGHT = '╗'
DOUBLE_BOTTOM_LEFT = '╚'
DOUBLE_BOTTOM_RIGHT = '╝'

class UiBox(UiGizmo):
    def __init__(self, position: UiCoord, size: UiSize, origin: UiOrigin = UiOrigin.TOP_LEFT):
        super().__init__()
        self._origin = origin
        self.set_position(position)
        self.set_size(size)
        self.tile = UiTile(self.get_size())

        self._top_left = UiChar(LIGHT_TOP_LEFT)
        self._top_right = UiChar(LIGHT_TOP_RIGHT)
        self._bottom_left = UiChar(LIGHT_BOTTOM_LEFT)
        self._bottom_right = UiChar(LIGHT_BOTTOM_RIGHT)
        self._horizontal = UiChar(LIGHT_HORIZONTAL)
        self._vertical = UiChar(LIGHT_VERTICAL)

    def draw(self, canvas: UiCharacterCanvas):
        top_left_pos = calc_location_with_offset(self.get_position(), self._origin, UiOrigin.TOP_LEFT, self.get_size())
        top_right_pos = calc_location_with_offset(self.get_position(), self._origin, UiOrigin.TOP_RIGHT, self.get_size())
        bottom_left_pos = calc_location_with_offset(self.get_position(), self._origin, UiOrigin.BOTTOM_LEFT, self.get_size())
        bottom_right_pos = calc_location_with_offset(self.get_position(), self._origin, UiOrigin.BOTTOM_RIGHT, self.get_size())

        canvas.draw_char(self._top_left, top_left_pos.x, top_left_pos.y)
        canvas.draw_char(self._top_right, top_right_pos.x, top_right_pos.y)
        canvas.draw_char(self._bottom_left, bottom_left_pos.x, bottom_left_pos.y)
        canvas.draw_char(self._bottom_right, bottom_right_pos.x, bottom_right_pos.y)

        for i in range(1, self.get_size().x - 1):
            canvas.draw_char(self._horizontal, top_left_pos.x + i, top_left_pos.y)
            canvas.draw_char(self._horizontal, top_left_pos.x + i, bottom_left_pos.y)

        for i in range(1, self.get_size().y - 1):
            canvas.draw_char(self._vertical, top_left_pos.x, top_left_pos.y + i)
            canvas.draw_char(self._vertical, top_right_pos.x, top_left_pos.y + i)

        top_right = self.geometry.get_inclusive_position_at(UiOrigin.TOP_RIGHT)
        canvas.draw_char(self._top_right, top_right.x, top_right.y)
        print()

        

    def change_origin(self, origin: UiOrigin):
        self.position = calc_location(self.get_position(), self._origin, origin, self.get_size())

UiLightBox = UiBox

class UiLightRoundBox(UiLightBox):
    def __init__(self, position: UiCoord, size: UiSize, origin: UiOrigin = UiOrigin.TOP_LEFT):
        super().__init__(position, size, origin)
        self._top_left.character = LIGHT_TOP_LEFT_CURVED
        self._top_right.character = LIGHT_TOP_RIGHT_CURVED
        self._bottom_left.character = LIGHT_BUTTOM_LEFT_CURVED
        self._bottom_right.character = LIGHT_BOTTOM_RIGHT_CURVED

class UiHeavyBox(UiBox):
    def __init__(self, position: UiCoord, size: UiSize, origin: UiOrigin = UiOrigin.TOP_LEFT):
        super().__init__(position, size, origin)
        self._top_left.character = HEAVY_TOP_LEFT
        self._top_right.character = HEAVY_TOP_RIGHT
        self._bottom_left.character = HEAVY_BOTTOM_LEFT
        self._bottom_right.character = HEAVY_BOTTOM_RIGHT
        self._horizontal.character = HEAVY_HORIZONTAL
        self._vertical.character = HEAVY_VERTICAL

class UiDoubleBox(UiBox):
    def __init__(self, position: UiCoord, size: UiSize, origin: UiOrigin = UiOrigin.TOP_LEFT):
        super().__init__(position, size, origin)
        self._top_left.character = DOUBLE_TOP_LEFT
        self._top_right.character = DOUBLE_TOP_RIGHT
        self._bottom_left.character = DOUBLE_BOTTOM_LEFT
        self._bottom_right.character = DOUBLE_BOTTOM_RIGHT
        self._horizontal.character = DOUBLE_HORIZONTAL
        self._vertical.character = DOUBLE_VERTICAL
