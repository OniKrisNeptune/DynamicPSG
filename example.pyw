import PySimpleGUI as sg
import DynamicPSG

# define layouts normally
layout_hi = [[sg.Button("Hi")]]
layout_bye = [[sg.Button("Bye")]]

# initialise a "dyndow"(dynamic window)
# give it a dictionary of layouts
dyndow = DynamicPSG.dyndow({
    "Hi": layout_hi,
    "Bye": layout_bye})

# start the window(basically sg.Window())
dyndow.start(title="My first window!", start="Hi")

while True: # normal event loop
    event, values = dyndow.read() # same as window.read()
    match event:
        case "Hi":
            dyndow.set("Bye") # change layout
        case "Bye":
            dyndow.set("Hi")
        case sg.WIN_CLOSED:
            dyndow.close() # same as window.close()
            break
