import tkinter as tk
from tkinter.font import NORMAL
import graph_canvas_function
import graph_left_frame
import keyboard1


def graph_gui(window) :
    # Dividing window into parts (frames,canvas)
    canvas = tk.Canvas (master = window, height = 800, width = 1130, background='yellow')
    left_frame = tk.Frame (master=window, height =300, width = 350)
    left_down_frame= tk.Frame(master=window,height=350,width=350,bg='white')
    right_frame = tk.Frame (master=window,height=800,width=50,bg='red')

    left_frame.grid (row=1,column=0,sticky='nw') #rowspan=10)
    canvas.grid(row=0,column=1,rowspan=10)
    left_down_frame.grid(row=9,column=0,sticky='s')
    right_frame.grid (row=0, column=2,rowspan=10)

    # reseting variable to default
    graph_left_frame.fun_no = 0
    graph_left_frame.entries = []
    graph_left_frame.labels = []
    
    #graph_right_frame.right_fun(right_frame)
    keyboard1.keyboard(window,left_down_frame,graph_left_frame.entries)
    graph_left_frame.plot_fun(left_frame)
    graph_canvas_function.raw (canvas,left_frame,graph_left_frame.entries,right_frame)

