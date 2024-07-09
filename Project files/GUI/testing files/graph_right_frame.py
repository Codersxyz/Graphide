import tkinter as tk

def right_fun (right_frame) :

    zoom_in = tk.Button (master=right_frame,text='+',font=('calibre',10,'bold'),width=4,height=2)
    zoom_in.grid(row=4,column=0,sticky='nw')

    zoom_out =  tk.Button (master=right_frame,text='-',font=('calibre',10,'bold'),width=4,height=2)
    zoom_out.grid(row=5,column=0,sticky='nw')
    