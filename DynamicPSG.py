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
        self.win = sg.Window(title, [self.sglayout], finalize=True)
        if start is None:
            start = self.namelist[0]
        if self.current is None:
            self.current = "_"+self.namelist[0]
        self.set(start)

    def set(self, layout):
        self.win[self.current].update(visible=False)
        self.current = "_"+layout
        self.win[self.current].update(visible=True)
        self.win.refresh()

    def read(self):
        return self.win.read()

    def close(self):
        self.win.close()
