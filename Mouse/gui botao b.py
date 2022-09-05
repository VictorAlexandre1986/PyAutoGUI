from tkinter import *

root = Tk()

def keyB(event):
    print("B pressionado")
    
def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress-B>",keyB)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

print('Primeiro clique na janela que abriu.')

root.mainloop()
