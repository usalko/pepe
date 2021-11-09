import os
from logging import Logger
from typing import AnyStr

import cv2
import numpy as np
import PySimpleGUI as sg


class Seek:

    def __init__(self, folder: str = '.'):
        self.folder = folder
        self.logger = Logger(__file__)

    def _read_image_file(self, filename: str) -> AnyStr:
        frame = cv2.imread(filename)
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        return imgbytes

    def _event_loop(self, window):
        while True:
            event, values = window.read()
            if event == 'Exit' or event == sg.WIN_CLOSED:
                break
            # Folder name was filled in, make a list of files in the folder
            if event == '-FOLDER-':
                self.folder = values['-FOLDER-']
                try:
                    # Get list of files in folder
                    file_list = os.listdir(self.folder)
                except:
                    file_list = []

                fnames = [
                    f
                    for f in file_list
                    if os.path.isfile(os.path.join(self.folder, f))
                    and f.lower().endswith(('.png', '.gif', '.jpeg', 'jpg'))
                ]
                window['-FILE LIST-'].update(fnames)
            elif event == '-FILE LIST-':  # A file was chosen from the listbox
                try:
                    filename = os.path.join(
                        values['-FOLDER-'], values['-FILE LIST-'][0]
                    )
                    window['-TOUT-'].update(filename)
                    window['-IMAGE-'].update(data=self._read_image_file(filename))
                except BaseException as e:
                    self.logger.error(e, exc_info=True)
                    pass

    def run(self):
        sg.theme('LightGreen')
        # The window layout in 2 columns
        file_list_column = [
            [
                sg.Text('Image Folder'),
                sg.In(size=(25, 1), enable_events=True, key='-FOLDER-'),
                sg.FolderBrowse(),
            ],
            [
                sg.Listbox(
                    values=[], enable_events=True, size=(40, 20), key='-FILE LIST-'
                )
            ],
        ]
        # For now will only show the name of the file that was chosen
        image_viewer_column = [
            [sg.Text('Choose an image from list on left:')],
            [sg.Text(size=(40, 1), key='-TOUT-')],
            [sg.Image(key='-IMAGE-')],
        ]
        # ----- Full layout -----
        layout = [
            [
                sg.Column(file_list_column),
                sg.VSeperator(),
                sg.Column(image_viewer_column),
            ]
        ]

        window = sg.Window('Pepe seek', layout)

        self._event_loop(window)

        window.close()


if __name__ == '__main__':
    Seek().run()
