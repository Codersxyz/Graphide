import tkinter as tk
import histogram_fun 


def Histogram (window) :
    left_frame = tk.Frame(master=window,width=351,height=741)
    left_frame.place (x=0,y=59,anchor='nw')

    canvas = tk.Canvas(master=window,width=1165,height=800,bg='white')
    canvas.place(x=355,y=0)

    label = tk.Label(master=left_frame,width=10,height=2,text='Enter data :')
    label.grid(row=0,column=0)

    # text box for data input
    text_box = tk.Text(master=left_frame,width=30,height=15,font=('arial',12,'normal'))
    text_box.grid (row=1,column=0)

    # draw button
    plot = tk.Button(master=left_frame,width=49,height=3,text='Create',command=lambda:histogram_fun.hist_fun(canvas,text_box))
    plot.grid(row=2,column=0)
    
    window.mainloop()