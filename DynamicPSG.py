import PySimpleGUI as sg

class dyndow:
    namelist = []
    sglayout = []
    current = None

    def __init__(self, layouts):
        for i in layouts:
            self.sglayout.append(sg.Column(layouts[i], key="_"+i, visible=False))
            self.namelist.append(i)

    def start(self, title = "", start = None):
        self.window = sg.Window(title, [self.sglayout], finalize=True)
        if start is None:
            start = self.namelist[0]
        if self.current is None:
            self.current = "_"+self.namelist[0]
        self.set(start)

    def set(self, layout):
        self.layout().update(visible=False)
        self.current = "_"+layout
        self.layout().update(visible=True)
        self.win().refresh()

    def read(self):
        return self.win().read()

    def close(self):
        self.win().close()

    def win(self):
        return self.window

    def layout(self):
        return self.win()[self.current]
