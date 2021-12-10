from tkinter import *
from opencc import OpenCC

root = Tk() # open new window
root.title('繁簡字轉換器') # set title
root.geometry('800x600') # set window size

# set key bindings
def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==88 and  ctrl and event.keysym.lower() != "x": 
        event.widget.event_generate("<<Cut>>")

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")

root.bind_all("<Key>", _onKeyRelease, "+")

# clear all text boxes
def clear():
    entry.delete(1.0, END)
    output.delete(1.0, END)

# simplified to traditional
def s2tw():
    cc = OpenCC('s2tw')
    simplified_text = entry.get(1.0, END)
    traditional_text = cc.convert(simplified_text)
    output.insert(END, traditional_text)

# traditional to simplified
def t2s():
    cc = OpenCC('t2s')
    traditional_text = entry.get(1.0, END)
    simplified_text = cc.convert(traditional_text)
    output.insert(END, simplified_text)

# label for entry
entry_label = Label(root, text="在此輸入")
entry_label.pack(pady=10)

# textbox of entry
entry = Text(root, width=100, height=10, borderwidth=5)
entry.pack(pady=20)

# initialize button object
button_frame = Frame(root)
button_frame.pack()

# create translate(t2s) button
translate_button = Button(button_frame, text='繁轉簡', command=t2s)
translate_button.grid(row=0, column=0)

# create translate(s2tw) button
translate_button = Button(button_frame, text='簡轉繁', command=s2tw)
translate_button.grid(row=0, column=1)

# create clear button
clear_button = Button(button_frame, text='清除', command=clear)
clear_button.grid(row=0, column=2)

# label for translation result
output_label = Label(root, text="翻譯結果")
output_label.pack(pady=10)

# textbox of result
output = Text(root, width=100, height=10, borderwidth=5)
output.pack(pady=20)

root.mainloop()
