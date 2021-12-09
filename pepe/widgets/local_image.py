from remi.gui import *
from time import time
from model.image_svg_model import ImageSvgModel

class LocalImage(Image):

    def __init__(self, file_path_name=None, **kwargs):
        super(LocalImage, self).__init__('/assets/please-select-image.png', **kwargs)

        self.model = ImageSvgModel()
        self.imagedata = None
        self.mimetype = None
        self.encoding = None
        self.load(file_path_name if file_path_name else './assets/please-select-image.png')

    def load(self, file_path_name):
        self.mimetype, self.encoding = mimetypes.guess_type(file_path_name)
        with open(file_path_name, 'rb') as f:
            self.imagedata = f.read()
        self.refresh()

    def refresh(self):
        i = int(time() * 1e6)
        self.attributes['src'] = "/%s/get_image_data?update_index=%d" % (
            id(self), i)

    def get_image_data(self, update_index):
        headers = {
            'Content-type': self.mimetype if self.mimetype else 'application/octet-stream'}
        return [self.imagedata, headers]

    def clear(self):
        self.load('./assets/please-select-image.png')
