from remi.gui import *
from os.path import basename, dirname, join, exists, isfile
from time import time
from model.image_svg_model import ImageSvgModel

class LocalImage(Image):

    def __init__(self, file_path_name=None, **kwargs):
        super(LocalImage, self).__init__('/assets/please-select-image.png', **kwargs)

        self.model = ImageSvgModel()
        self.imagedata = None
        self.mimetype = None
        self.encoding = None
        self.svg_index = None
        self.file_path = None
        self.load(file_path_name if file_path_name else './assets/please-select-image.png')

    def load(self, file_path):
        self.file_path = file_path
        self.mimetype, self.encoding = mimetypes.guess_type(file_path)
        with open(file_path, 'rb') as f:
            self.imagedata = f.read()
        # Try to read svg index
        svg_index_path = join(dirname(file_path), '.' + basename(file_path) + '.svg')
        if exists(svg_index_path) and isfile(svg_index_path):
            with open(svg_index_path, 'rb') as f:
                self.svg_index = f.read().decode('utf-8')
        self.refresh()

    def refresh(self):
        i = int(time() * 1e6)
        self.attributes['src'] = "/%s/get_image_data?update_index=%d" % (
            id(self), i)

    def get_image_data(self, update_index):
        headers = {
            'Content-type': self.mimetype if self.mimetype else 'application/octet-stream'}
        return [self.imagedata, headers]

    def save(self):
        file_path = self.file_path
        svg_index_path = join(dirname(file_path), '.' + basename(file_path) + '.svg')
        if self.svg_index and exists(file_path) and (not exists(svg_index_path) or isfile(svg_index_path)):
            with open(svg_index_path, 'wb') as f:
                f.write(str.encode(self.svg_index))

    def clear(self):
        self.load('./assets/please-select-image.png')
