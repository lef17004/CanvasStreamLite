from .uivector import UiCoord, UiSize
from .uiorigin import UiOrigin, calc_location

class UiGeometry:
    def __init__(self, position: UiCoord = None, size: UiSize = None):
        if position:
            self.position = position # Top Left
        else:
            self.position = UiCoord()

        if size:
            self.size = size
        else:
            self.size = UiSize()
    
    def is_in_bounds(self, position: UiCoord):
        top_left = self.position
        bottom_right = self.get_exclusive_position_at(UiOrigin.BOTTOM_RIGHT)
        if (top_left.x <= position.x and position.x <= bottom_right.x and 
            top_left.y <= position.y and position.y <= bottom_right.y):
            return True
        return False
            

    def get_exclusive_position_at(self, origin: UiOrigin) -> UiCoord:
        return calc_location(self.position, UiOrigin.TOP_LEFT, origin, self.size)
    
    def get_inclusive_position_at(self, origin: UiOrigin) -> UiCoord:
        location = self.get_exclusive_position_at(origin)
        if origin == UiOrigin.TOP_RIGHT or origin == UiOrigin.BOTTOM_RIGHT:
            location.x -= 1

        if origin == UiOrigin.BOTTOM_LEFT or origin == UiOrigin.BOTTOM_RIGHT:
            location.y -= 1

        return location
    
    def get_top_left(self) -> UiCoord:
        return self.position.copy()
    
    def get_top_center(self) -> UiCoord:
        position = self.position.copy()
        position.x += self.size.x / 2

    def get_top_right(self) -> UiCoord:
        position = self.position.copy()
        position.x += self.size.x

    def get_center_left(self) -> UiCoord:
        position = self.position.copy()
        position.y += self.size.y / 2
    
    def get_center(self) -> UiCoord:
        position = self.position.copy()
        position.x += self.size.x / 2
        position.y += self.size.y / 2

    def get_center_right(self) -> UiCoord:
        position = self.position.copy()
        position.x += self.size.x
        position.y += self.size.y / 2

    def get_bottom_left(self) -> UiCoord:
        position = self.position.copy()
        position.y += self.size.y
    
    def get_bottom_center(self) -> UiCoord:
        position = self.position.copy()
        position.x += self.size.x / 2
        position.y += self.size.y

    def get_bottom_right(self) -> UiCoord:
        position = self.position.copy()
        position.x += self.size.x
        position.y += self.size.y


    





# def calc_location_at(new_origin: UiOrigin, geometry: UiGeometry):
#     top_left_location = convert_to_top_left(geometry)
#     new_geometry = UiGeometry()
#     # new_geometry.size = geometry.size
#     # new_geometry.position = top_left_location
#     # new_geometry.origin = geometry.origin
#     new_location = convert_top_left_to(new_origin, geometry)
#     return new_location

# def calc_location_with_offset(current_location, current_orgin, new_origin, size):
#     top_left_location = convert_to_top_left(current_orgin, current_location, size)
#     new_location = convert_top_left_to(new_origin, top_left_location, size)
#     if new_origin == UiOrigin.TOP_RIGHT or new_origin == UiOrigin.BOTTOM_RIGHT:
#         new_location.x -= 1

#     if new_origin == UiOrigin.BOTTOM_LEFT or  new_origin == UiOrigin.BOTTOM_RIGHT:
#         new_location.y -= 1

#     return new_location
        

# def convert_to_top_left(geometry: UiGeometry) -> UiCoord:
#     if geometry.origin == UiOrigin.TOP_LEFT:
#         return geometry.position
#     elif geometry.origin == UiOrigin.TOP_CENTER:
#         return top_center_to_top_left(geometry.position, geometry.size)
#     elif geometry.origin == UiOrigin.TOP_RIGHT:
#         return top_right_to_top_left(geometry.position, geometry.size)
#     elif geometry.origin == UiOrigin.CENTER_LEFT:
#         return center_left_to_top_left(geometry.position, geometry.size)
#     elif geometry.origin == UiOrigin.CENTER:
#         return center_to_top_left(geometry.position, geometry.size)
#     elif geometry.origin == UiOrigin.CENTER_RIGHT:
#         return center_right_to_top_left(geometry.position, geometry.size)
#     elif geometry.origin == UiOrigin.BOTTOM_LEFT:
#         return bottom_left_to_top_left(geometry.position, geometry.size)
#     elif geometry.origin == UiOrigin.BOTTOM_CENTER:
#         return bottom_center_to_top_left(geometry.position, geometry.size)
#     elif geometry.origin == UiOrigin.BOTTOM_RIGHT:
#         return bottom_right_to_top_left(geometry.position, geometry.size)
#     else:
#         assert False, "Should not reach here."
     

# def convert_top_left_to(new_origin, geometry: UiGeometry):
#     if new_origin == UiOrigin.TOP_LEFT:
#         return geometry.position
#     elif new_origin == UiOrigin.TOP_CENTER:
#         return top_left_to_top_center(geometry.position, geometry.size)
#     elif new_origin == UiOrigin.TOP_RIGHT:
#         return top_left_to_top_right(geometry.position, geometry.size)
#     elif new_origin == UiOrigin.CENTER_LEFT:
#         return top_left_to_center_left(geometry.position, geometry.size)
#     elif new_origin == UiOrigin.CENTER:
#         return top_left_to_center(geometry.position, geometry.size)
#     elif new_origin == UiOrigin.CENTER_RIGHT:
#         return top_left_to_center_right(geometry.position, geometry.size)
#     elif new_origin == UiOrigin.BOTTOM_LEFT:
#         return top_left_to_bottom_left(geometry.position, geometry.size)
#     elif new_origin == UiOrigin.BOTTOM_CENTER:
#         return top_left_to_bottom_center(geometry.position, geometry.size)
#     elif new_origin == UiOrigin.BOTTOM_RIGHT:
#         return top_left_to_bottom_right(geometry.position, geometry.size)
#     else:
#         assert False, "Output should not reach here."


# # 0--1--2
# # |     |
# # 3  4  5
# # |     |
# # 6--7--8

# # 0 -> 1
# def top_left_to_top_center(location: UiCoord, size: UiSize):
#     return UiCoord(location.x + (size.x / 2), location.y)

# # 0 -> 2
# def top_left_to_top_right(location: UiCoord, size: UiSize):
#     return UiCoord(location.x + size.x, location.y)

# # 0 -> 3
# def top_left_to_center_left(location: UiCoord, size: UiSize):
#     return UiCoord(location.x, location.y + (size.y / 2))

# # 0 -> 4
# def top_left_to_center(location: UiCoord, size: UiSize):
#     return UiCoord(location.x + (size.x / 2), location.y + (size.y / 2))

# # 0 -> 5
# def top_left_to_center_right(location: UiCoord, size: UiSize):
#     return UiCoord(location.x + size.x, location.y + (size.y / 2))

# # 0 -> 6
# def top_left_to_bottom_left(location: UiCoord, size: UiSize):
#     return UiCoord(location.x, location.y + size.y)

# # 0 -> 7
# def top_left_to_bottom_center(location: UiCoord, size: UiSize):
#     return UiCoord(location.x + (size.x / 2), location.y + size.y)

# # 0 -> 8
# def top_left_to_bottom_right(location: UiCoord, size: UiSize):
#     return UiCoord(location.x + size.x, location.y + size.y)

# # 0 <- 1
# def top_center_to_top_left(location: UiCoord, size: UiSize):
#     return UiCoord(location.x - (size.x / 2), location.y)

# # 0 <- 2
# def top_right_to_top_left(location: UiCoord, size: UiSize):
#     return UiCoord(location.x - size.x, location.y)

# # 0 <- 3
# def center_left_to_top_left(location: UiCoord, size: UiSize):
#     return UiCoord(location.x, location.y - (size.y / 2))

# # 0 <- 4
# def center_to_top_left(location: UiCoord, size: UiSize):
#     return UiCoord(location.x - (size.x / 2), location.y - (size.y / 2))

# # 0 <- 5
# def center_right_to_top_left(location: UiCoord, size: UiSize):
#     return UiCoord(location.x - size.x, location.y - (size.y / 2))

# # 0 <- 6
# def bottom_left_to_top_left(location: UiCoord, size: UiSize):
#     return UiCoord(location.x, location.y - size.y)

# # 0 <- 7
# def bottom_center_to_top_left(location: UiCoord, size: UiSize):
#     return UiCoord(location.x - (size.x / 2), location.y - size.y)

# # 0 <- 8
# def bottom_right_to_top_left(location: UiCoord, size: UiSize):
#     return UiCoord(location.x - size.x, location.y - size.y)