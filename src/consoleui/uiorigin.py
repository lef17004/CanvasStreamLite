from enum import IntEnum, auto
from .uivector import UiCoord, UiSize

class UiOrigin(IntEnum):
    TOP_LEFT = auto()
    TOP_CENTER = auto()
    TOP_RIGHT = auto()
    CENTER_LEFT = auto()
    CENTER = auto()
    CENTER_RIGHT = auto()
    BOTTOM_LEFT = auto()
    BOTTOM_CENTER = auto()
    BOTTOM_RIGHT = auto()

def calc_location(current_location, current_orgin, new_origin, size):
    top_left_location = convert_to_top_left(current_orgin, current_location, size)
    new_location = convert_top_left_to(new_origin, top_left_location, size)
    return new_location

def calc_location_with_offset(current_location, current_orgin, new_origin, size):
    top_left_location = convert_to_top_left(current_orgin, current_location, size)
    new_location = convert_top_left_to(new_origin, top_left_location, size)
    if new_origin == UiOrigin.TOP_RIGHT or new_origin == UiOrigin.BOTTOM_RIGHT:
        new_location.x -= 1

    if new_origin == UiOrigin.BOTTOM_LEFT or  new_origin == UiOrigin.BOTTOM_RIGHT:
        new_location.y -= 1

    return new_location
        

def convert_to_top_left(origin, current_location, size):
    if origin == UiOrigin.TOP_LEFT:
        return current_location
    elif origin == UiOrigin.TOP_CENTER:
        return top_center_to_top_left(current_location, size)
    elif origin == UiOrigin.TOP_RIGHT:
        return top_right_to_top_left(current_location, size)
    elif origin == UiOrigin.CENTER_LEFT:
        return center_left_to_top_left(current_location, size)
    elif origin == UiOrigin.CENTER:
        return center_to_top_left(current_location, size)
    elif origin == UiOrigin.CENTER_RIGHT(current_location, size):
        return center_right_to_top_left(current_location, size)
    elif origin == UiOrigin.BOTTOM_LEFT(current_location, size):
        return bottom_left_to_top_left(current_location, size)
    elif origin == UiOrigin.BOTTOM_CENTER(current_location, size):
        return bottom_center_to_top_left(current_location, size)
    elif origin == UiOrigin.BOTTOM_RIGHT(current_location, size):
        return bottom_right_to_top_left(current_location, size)
    else:
        assert False, "Should not reach here."
     

def convert_top_left_to(new_origin, current_location, size):
    if new_origin == UiOrigin.TOP_LEFT:
        return current_location
    elif new_origin == UiOrigin.TOP_CENTER:
        return top_left_to_top_center(x, size)
    elif new_origin == UiOrigin.TOP_RIGHT:
        return top_left_to_top_right(current_location, size)
    elif new_origin == UiOrigin.CENTER_LEFT:
        return top_left_to_center_left(current_location, size)
    elif new_origin == UiOrigin.CENTER:
        return top_left_to_center(current_location, size)
    elif new_origin == UiOrigin.CENTER_RIGHT:
        return top_left_to_center_right(current_location, size)
    elif new_origin == UiOrigin.BOTTOM_LEFT:
        return top_left_to_bottom_left(current_location, size)
    elif new_origin == UiOrigin.BOTTOM_CENTER:
        return top_left_to_bottom_center(current_location, size)
    elif new_origin == UiOrigin.BOTTOM_RIGHT:
        return top_left_to_bottom_right(current_location, size)
    else:
        assert False, "Output should not reach here."


# 0--1--2
# |     |
# 3  4  5
# |     |
# 6--7--8

# 0 -> 1
def top_left_to_top_center(location: UiCoord, size: UiSize):
    return UiCoord(location.x + (size.x / 2), location.y)

# 0 -> 2
def top_left_to_top_right(location: UiCoord, size: UiSize):
    return UiCoord(location.x + size.x, location.y)

# 0 -> 3
def top_left_to_center_left(location: UiCoord, size: UiSize):
    return UiCoord(location.x, location.y + (size.y / 2))

# 0 -> 4
def top_left_to_center(location: UiCoord, size: UiSize):
    return UiCoord(location.x + (size.x / 2), location.y + (size.y / 2))

# 0 -> 5
def top_left_to_center_right(location: UiCoord, size: UiSize):
    return UiCoord(location.x + size.x, location.y + (size.y / 2))

# 0 -> 6
def top_left_to_bottom_left(location: UiCoord, size: UiSize):
    return UiCoord(location.x, location.y + size.y)

# 0 -> 7
def top_left_to_bottom_center(location: UiCoord, size: UiSize):
    return UiCoord(location.x + (size.x / 2), location.y + size.y)

# 0 -> 8
def top_left_to_bottom_right(location: UiCoord, size: UiSize):
    return UiCoord(location.x + size.x, location.y + size.y)

# 0 <- 1
def top_center_to_top_left(location: UiCoord, size: UiSize):
    return UiCoord(location.x - (size.x / 2), location.y)

# 0 <- 2
def top_right_to_top_left(location: UiCoord, size: UiSize):
    return UiCoord(location.x - size.x, location.y)

# 0 <- 3
def center_left_to_top_left(location: UiCoord, size: UiSize):
    return UiCoord(location.x, location.y - (size.y / 2))

# 0 <- 4
def center_to_top_left(location: UiCoord, size: UiSize):
    return UiCoord(location.x - (size.x / 2), location.y - (size.y / 2))

# 0 <- 5
def center_right_to_top_left(location: UiCoord, size: UiSize):
    return UiCoord(location.x - size.x, location.y - (size.y / 2))

# 0 <- 6
def bottom_left_to_top_left(location: UiCoord, size: UiSize):
    return UiCoord(location.x, location.y - size.y)

# 0 <- 7
def bottom_center_to_top_left(location: UiCoord, size: UiSize):
    return UiCoord(location.x - (size.x / 2), location.y - size.y)

# 0 <- 8
def bottom_right_to_top_left(location: UiCoord, size: UiSize):
    return UiCoord(location.x - size.x, location.y - size.y)