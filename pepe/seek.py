import PySimpleGUI as sg


class Seek:

    def run(self):
        sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()


if __name__ == '__main__':
    Seek().run()