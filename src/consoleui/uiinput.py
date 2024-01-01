from enum import IntEnum, auto
from dataclasses import dataclass

class InputType(IntEnum):
    CLICK = auto()

@dataclass
class UiInput:
    type: InputType = InputType.CLICK
    x: int = 0
    y: int = 0