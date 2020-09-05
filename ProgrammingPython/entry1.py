from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import LEFT
from tkinter import TOP
from tkinter import RIGHT
from tkinter import X

from quitter import Quitter

def fetch():
    print('Input => "%s"' % ent.get())             # get text

root = Tk()
ent = Entry(root)
ent.insert(0, 'Type words here')                   # set text
ent.pack(side=TOP, fill=X)                         # grow horiz

ent.focus()                                        # save a click
ent.bind('<Return>', (lambda event: fetch()))      # on enter key
btn = Button(root, text='Fetch', command=fetch)    # and on button
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()
