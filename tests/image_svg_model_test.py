from unittest import TestCase
from pepe.model.image_svg_model import ImageSvgModel
from os.path import join, dirname

# For more tests see http://tutorials.jenkov.com/svg/svg-viewport-view-box.html
#                    https://www.w3.org/TR/SVG/struct.html
#                    https://github.com/hogesonline/svg_play/
class ImageSvgModelTest(TestCase):

    def test(self):
        sample_image_1_path = join(dirname(__file__), 'data', 'sample-image-1.svg')
        ImageSvgModel.from_file(sample_image_1_path)
        self.assertTrue(True)