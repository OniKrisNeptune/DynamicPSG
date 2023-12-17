# Dynamic layouts for PySimpleGUI

# proj descripton

uses psg, specifically the ability of columns to be hidden. The window itself is actually some columns with the layouts and the one that should currrently be active is visible.  the rest are hidden.

# Guide
# example code

```py
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
```

# Call reference
## \_\_init__()
*added in v0.1.0*

```
DynamicPSG.dyndow(
    layouts
    )
```
Name | Type | Meaning
--- | --- | ---
layouts | dict{str(Name): list(layout)} | Creates the dynamic window object.

## close()
*added in v0.1.0*

Replaces `window.close()`
```
dyndow.close()
```

## read()
*added in v0.1.0*

Replaces `window.read()`

```
dyndow.read()
```
### return
Name | Type | Meaning
--- | --- | ---
event | any | event
values | list or dict | values

## set()
*added in v0.1.0*

```
dyndow.set(
    name
    )
```
Name | Type | Meaning
--- | --- | ---
name | str | name of the layout to change the window to

## start()
*added in v0.1.0*

Simular/replaces `sg.Window()`

```
dyndow.start(
    title = ""
    start = None
    )
```
Name | Type | Meaning | Default
--- | --- | --- | ---
title | str | Title of the window. | Empty
start | str | Name of the layout to start with. | First layout entered in \_\_init__

## win()
*added in v0.2.0*

if, for whatever reason you need to access psg's window object, use this. 
The contents of the window are columns that the library manages, not your layout.
To access your layout, use `dyndow.layout()`

```
dyndow.win()
```
### return
Name | Type | Meaning
--- | --- | ---
layout | sg.Window() | the gui window object

## layout()
*added in v0.2.0*

returns the layout being used at the moment.

```
dyndow.layout(
    index = None
    )
```
Name | Type | Meaning | Default
--- | --- | --- | ---
index | str | Name of layout to return | Currently active layout

### return
Name | Type | Meaning
--- | --- | ---
layout | sg.Column | Your layout, stored in a column
