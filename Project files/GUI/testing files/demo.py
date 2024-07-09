from re import X
import tkinter as tk
from tkinter.font import NORMAL
import keyboard1
import graph_canvas_function

# Creating the Main Window
window = tk.Tk()
window.title ("Graphite")
window.geometry ('1920x1000')

# Dividing window into parts (frames,canvas)
canvas = tk.Canvas (master = window, height = 800, width = 1130, background='yellow')
left_frame = tk.Frame (master=window, height =400, width = 350)
left_down_frame= tk.Frame(master=window,height=400,width=350,bg='#ffffff')
right_frame = tk.Frame (master=window,height=800,width=50,bg='red')


# Drop down menu for choosing between various graphs

options = ('Graph','Bar Graph', 'Histrogram', 'Line Graph', 'Pie Chart')
clicked = tk.StringVar()
clicked.set(options[0])

def choosed (choice) :
    choice = clicked.get ()

# Creating the drop down menu
drop_menu = tk.OptionMenu(window, clicked, *options, command= choosed)
drop_menu.config(width=29,height=2,border=0.5,font=('Times New Roman',15,'normal'))
drop_menu.grid (row=0,column=0,columnspan=2,pady=2,sticky='nw')

left_frame.grid (row=1,column=0) #rowspan=10)
canvas.grid(row=0,column=1,rowspan=3)
left_down_frame.grid(row=2,column=0)
right_frame.grid (row=0, column=2,rowspan=3)

label = tk.Label(master=left_frame,width=5,height=1,border=0.5,text='F')
label.pack

keyboard1.keyboard(left_down_frame)
graph_canvas_function.raw(canvas)
    
window.mainloop()
