from __future__ import annotations

class UiColor:
    def __init__(self, name, hex_code):
        self.name:str = name
        self.hex_code:str = hex_code

    def __eq__(self, other: UiColor):
        return self.name == other.name and self.hex_code == other.hex_code

class Black(UiColor):
    def __init__(self):
        super().__init__("Black", "#000000")

class White(UiColor):
    def __init__(self):
        super().__init__("White", "#000000")

    