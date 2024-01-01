from __future__ import annotations
from dataclasses import dataclass
from dataclasses import field
from .uicolor import UiColor, Black, White

@dataclass
class UiStyle:
    is_bold: bool= False
    is_italic: bool = False
    is_underlined: bool = False
    foreground_color: UiColor = field(default_factory=Black)
    background_color: UiColor = field(default_factory=White)

    def __eq__(self, other: UiStyle):
        return self.is_bold == other.is_bold and self.is_italic == other.is_italic and self.is_underlined == other.is_underlined and self.foreground_color == other.foreground_color and self.background_color == other.background_color
