from .uichar import UiChar
from .uivector import UiSize

class UiTile:
    def __init__(self, size: UiSize):
        self.data = self._create_data(size)
    
    def resize(self, size: UiSize):
        new_data = self._create_data(size)

        num_rows = len(self.data) if len(self.data) < len(new_data) else len(new_data)
        num_cols = len(self.data[0]) if len(self.data[0]) < len(new_data[0]) else len(new_data[0])

        for row in range(num_rows):
            for col in range(num_cols):
                new_data[row][col] = self.data[row][col]

        self.data = new_data


    def _create_data(self, size: UiSize):
        data = []
        for _ in range(size.y):
            row_list = []
            data.append(row_list)
            for _ in range(size.x):
                row_list.append(UiChar(''))
        return data