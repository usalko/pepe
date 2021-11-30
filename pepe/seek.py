
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App
from os import listdir
from os.path import join
from functools import reduce
from operator import iconcat


class PepeApp(App):
    file_list: ListView = None

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
        svg_glass: Svg = widget
        svg_glass.append(SvgCircle(x, y, 30))
        print(f'Image mouse down ({x}, {y})!')
        svg_glass.redraw()

    def on_folder_selected(self, widget, folder_item_widget, folder_item):
        self.file_list.empty()
        for name, full_path in reduce(iconcat, [[(name, join(f, name)) for name in listdir(f)] for f in folder_item], []):
            self.file_list.append(value=name, key=full_path)

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
        e_image = Image()
        e_image.attr_class = 'Image'
        e_image.attr_editor_newclass = False
        e_image.attr_src = ''
        e_image.css_align_content = 'flex-start'
        e_image.css_height = '100%'
        e_image.css_left = '20%'
        e_image.css_position = 'static'
        e_image.css_top = '0px'
        e_image.css_width = '100%'
        e_image.variable_name = 'image0'
        image_container.append(e_image, 'image0')
        svg_glass = Svg()
        svg_glass.attr_class = 'Svg'
        svg_glass.attr_editor_newclass = False
        svg_glass.css_align_content = 'flex-start'
        svg_glass.css_height = '100%'
        svg_glass.css_left = '20%'
        svg_glass.css_position = 'absolute'
        svg_glass.css_top = '0px'
        svg_glass.css_width = '80%'
        svg_glass.variable_name = 'svg0'
        image_container.append(svg_glass, 'svg0')
        hbox0.append(image_container, 'container1')
        container0.append(hbox0, 'hbox0')

        # Setup logic
        svg_glass.onmousedown.do(self.on_img_mousedown)

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
