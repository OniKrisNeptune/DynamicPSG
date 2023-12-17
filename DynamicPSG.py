import PySimpleGUI as sg

class dyndow:
    namelist = []
    sglayout = []
    current = None
    active = False
    nooftemps = 0

    def __init__(self, layouts):
        self.add(layouts)

    def start(self, title = "", start = None):
        self.active = True
        self.window = sg.Window(title, [self.sglayout], finalize=True)
        if start is None:
            start = self.namelist[0]
        if self.current is None:
            self.current = "_"+self.namelist[0]
        self.set(start)

    def add(self, layouts, temp = False):
        for i in layouts:
            layout = sg.Column(layouts[i], key="_"+i, visible=False)
            if self.active:
                self.win().extend_layout(self.win(), [layout])
            elif not temp:
                self.namelist.append(i)
                self.sglayout.append(layout)

    def set(self, layout):
        self.layout().update(visible=False)
        if type(layout) is str:
            self.current = "_"+layout
        else:
            layout = {"_"+self.nooftemps: layout[0]}
            self.nooftemps += 1
            self.add(layout, temp = True)
            self.current = "__"+layout[0]
        self.layout().update(visible=True)
        self.win().refresh()

    def read(self):
        return self.win().read()

    def close(self):
        self.active = False
        self.win().close()

    def win(self):
        return self.window

    def layout(self, index = None):
        if index is None:
            index = self.current
        return self.win()[index]
