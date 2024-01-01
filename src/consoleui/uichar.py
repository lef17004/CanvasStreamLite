from .uistyle import UiStyle

class UiChar:
    def __init__(self, char, style=None):
        self._character: str = char

        if style:
            self._style: UiStyle = style
        else:
            self._style = UiStyle()

    def apply_style(self, style: UiStyle):
        self._style = style

    @property
    def character(self)-> str:
        return self._character

    @character.setter
    def character(self, char: str):
        if char:
            self._character = char[0]

    @property
    def is_bold(self) -> bool:
        return self._style.is_bold

    @is_bold.setter
    def is_bold(self, value: bool):
        self._style.is_bold = value

    @property
    def is_italic(self) -> bool:
        return self._style.is_italic

    @is_italic.setter
    def is_italic(self, value: bool):
        self._style.is_italic = value

    @property
    def is_underlined(self) -> bool:
        return self._style.is_underlined

    @is_underlined.setter
    def is_underlined(self, value: bool):
        self._style.is_underlined = value

    @property
    def foreground_color(self):
        return self._style.foreground_color

    @foreground_color.setter
    def foreground_color(self, value):
        self._style.foreground_color = value

    @property
    def background_color(self):
        return self._style.background_color

    @background_color.setter
    def background_color(self, value):
        self._style.background_color = value
