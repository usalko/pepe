class ImageSvgModel:

    def __init__(self):
        self._store = {}

    @staticmethod
    def from_file(file_path: str):
        ...

    def add_point(self, x: float, y: float):
        ...
