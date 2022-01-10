
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App
from os import listdir
from os.path import join, isfile
from functools import reduce
from operator import iconcat
from traceback import format_exception
from widgets.svg_glass import SvgGlass
from widgets.local_image import LocalImage
from xmltodict import parse as xml_to_dict_parse


class PepeApp(App):
    file_list: ListView = None
    e_image: LocalImage = None
    svg_glass: SvgGlass = None

    def __init__(self, *args, **kwargs):
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(PepeApp, self).__init__(
                *args, static_file_path={'my_res': './res/'})

    def idle(self):
        # idle function called every update cycle
        pass

    def main(self):
        return PepeApp.construct_ui(self)

    def on_img_mousedown(self, widget, x, y):
        svg_glass: SvgGlass = widget
        # if it's the same point remove it instead add
        the_same_poly_list = svg_glass.has_the_same_center(x, y, 6)
        if the_same_poly_list:
            for the_same_poly in the_same_poly_list:
                svg_glass.remove_child(the_same_poly)
        else:
            dot = SvgCircle(x, y, 6)
            dot.set_stroke(width=2, color='orange')
            dot.set_fill(color='#00000000')
            svg_glass.append(dot)

        # Savepoint
        self.e_image.svg_index = svg_glass.repr()
        # TODO: use queue instead direct call
        self.e_image.save()
        # Set needs update flag to a true
        svg_glass.children.changed = True
        svg_glass.redraw()
        print(f'Image mouse down ({x}, {y})!')

    def on_folder_selected(self, widget, folder_item_widget, folder_item):
        self.file_list.empty()
        for name, full_path in reduce(iconcat, [[(name, join(f, name)) for name in listdir(f)] for f in folder_item], []):
            # Didn't show svg index for image
            if name.startswith('.') and name.endswith('.svg'):
                continue
            self.file_list.append(value=name, key=full_path)

    def _parse_svg_index(self, svg_index: dict):
        for key, value in svg_index.items():
            if key.startswith('@'):
                continue
            if key == 'circle':
                for svg_circle in value:
                    circle = SvgCircle(svg_circle['@cx'], svg_circle['@cy'], 6)
                    circle.set_stroke(width=2, color='orange')
                    circle.set_fill(color='#00000000')
                    self.svg_glass.append(circle)

    def on_item_selected(self, widget, folder_item_path: str):
        if isfile(folder_item_path):
            self.e_image.save()
            try:
                self.mimetype, self.encoding = mimetypes.guess_type(
                    folder_item_path)
                if not('image' in self.mimetype):
                    raise Exception(
                        f'Not an image, mime type is: {self.mimetype}')
                self.e_image.load(folder_item_path)

                self.svg_glass.clear()
                if self.e_image.svg_index:
                    svg_index = xml_to_dict_parse(self.e_image.svg_index)
                    self._parse_svg_index(svg_index['svg'])

                # Set needs update flag to a true
                self.svg_glass.children.changed = True
                self.svg_glass.redraw()
                self.e_image.refresh()
            except BaseException as e:
                print(
                    f'Error process folder item {folder_item_path}. Explanation: {format_exception(type(e), e, e.__traceback__)}')
                self.e_image.clear()
                self.svg_glass.clear()

    def onload(self, emitter):
        """ WebPage Event that occurs on webpage loaded
        """
        super(PepeApp, self).onload(emitter)
        self.e_image.clear()

    @staticmethod
    def construct_ui(self):
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        container0 = Container()
        container0.attr_class = 'Container'
        container0.attr_editor_newclass = False
        container0.css_height = 'calc(100% - 30px)'
        container0.css_left = '15.0px'
        container0.css_position = 'absolute'
        container0.css_top = '15.0px'
        container0.css_width = 'calc(100% - 30px)'
        container0.variable_name = 'container0'
        hbox0 = HBox()
        hbox0.attr_class = 'HBox'
        hbox0.attr_editor_newclass = False
        hbox0.css_align_items = 'center'
        hbox0.css_display = 'flex'
        hbox0.css_flex_direction = 'row'
        hbox0.css_height = '100%'
        hbox0.css_justify_content = 'space-around'
        hbox0.css_left = '0px'
        hbox0.css_position = 'absolute'
        hbox0.css_top = '0px'
        hbox0.css_width = '100%'
        hbox0.variable_name = 'hbox0'
        vbox0 = VBox()
        vbox0.attr_class = 'VBox'
        vbox0.attr_editor_newclass = False
        vbox0.css_align_items = 'center'
        vbox0.css_display = 'flex'
        vbox0.css_flex_direction = 'column'
        vbox0.css_height = '100%'
        vbox0.css_justify_content = 'space-around'
        vbox0.css_order = '-1'
        vbox0.css_position = 'static'
        vbox0.css_top = '0px'
        vbox0.css_width = '20%'
        vbox0.variable_name = 'vbox0'
        self.file_list = ListView()
        self.file_list.attr_class = 'ListView'
        self.file_list.attr_editor_newclass = False
        self.file_list.css_height = '80%'
        self.file_list.css_order = '-1'
        self.file_list.css_position = 'static'
        self.file_list.css_top = '0px'
        self.file_list.css_width = '100%'
        self.file_list.variable_name = 'listview0'
        self.file_list.onselection.do(self.on_item_selected)
        vbox0.append(self.file_list, 'listview0')
        filefoldernavigator = FileFolderNavigator()
        filefoldernavigator.allow_file_selection = False
        filefoldernavigator.allow_folder_selection = True
        filefoldernavigator.attr_class = 'FileFolderNavigator'
        filefoldernavigator.attr_editor_newclass = False
        filefoldernavigator.css_display = 'grid'
        filefoldernavigator.css_grid_template_areas = "'button_back url_editor button_go''items items items'"
        filefoldernavigator.css_grid_template_columns = '30px auto 30px'
        filefoldernavigator.css_grid_template_rows = '30px auto'
        filefoldernavigator.css_height = '20%'
        filefoldernavigator.css_order = '-1'
        filefoldernavigator.css_position = 'static'
        filefoldernavigator.css_top = '20px'
        filefoldernavigator.css_width = '100%'
        filefoldernavigator.multiple_selection = False
        filefoldernavigator.selection_folder = '.'
        filefoldernavigator.variable_name = 'filefoldernavigator0'
        filefoldernavigator.on_folder_item_selected.do(self.on_folder_selected)

        vbox0.append(filefoldernavigator, 'filefoldernavigator0')
        hbox0.append(vbox0, 'vbox0')
        image_container = Container()
        image_container.attr_class = 'Container'
        image_container.attr_editor_newclass = False
        image_container.css_height = '100%'
        image_container.css_order = '-1'
        image_container.css_position = 'static'
        image_container.css_top = '0px'
        image_container.css_width = '80%'
        image_container.variable_name = 'container1'
        self.e_image = LocalImage()
        self.e_image.attr_class = 'Image'
        self.e_image.attr_editor_newclass = False
        self.e_image.attr_src = ''
        self.e_image.css_align_content = 'flex-start'
        self.e_image.css_height = '100%'
        self.e_image.css_left = '20%'
        self.e_image.style['object-fit'] = 'scale-down'
        self.e_image.css_position = 'static'
        self.e_image.css_top = '0px'
        self.e_image.css_width = '100%'
        self.e_image.variable_name = 'image0'
        image_container.append(self.e_image, 'image0')
        self.svg_glass = SvgGlass()
        self.svg_glass.attr_class = 'Svg'
        self.svg_glass.attr_editor_newclass = False
        self.svg_glass.css_align_content = 'flex-start'
        self.svg_glass.css_height = '100%'
        self.svg_glass.css_left = '20%'
        self.svg_glass.css_position = 'absolute'
        self.svg_glass.css_top = '0px'
        self.svg_glass.css_width = '80%'
        self.svg_glass.variable_name = 'svg0'
        image_container.append(self.svg_glass, 'svg0')
        hbox0.append(image_container, 'container1')
        container0.append(hbox0, 'hbox0')

        # Setup logic
        self.svg_glass.onmousedown.do(self.on_img_mousedown)

        self.container0 = container0
        return self.container0


# Configuration
configuration = {'config_project_name': 'pepe',
                 'config_address': '0.0.0.0',
                 'config_port': 8081,
                 'config_multiple_instance': True,
                 'config_enable_file_cache': True,
                 'config_start_browser': True,
                 'config_resourcepath': './res/'}

if __name__ == '__main__':
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(PepeApp,
          address=configuration['config_address'],
          port=configuration['config_port'],
          multiple_instance=configuration['config_multiple_instance'],
          enable_file_cache=configuration['config_enable_file_cache'],
          start_browser=configuration['config_start_browser'])
