from operator import le
import tkinter as tk
from tkinter.font import NORMAL
#from GUI.graph_left_frame import abc
import graph_canvas_function
import graph_left_frame
import keyboard1
#import graph_right_frame


# Creating the Main Window
window = tk.Tk()
window.title ("Graphite")
window.geometry ('1920x1000')

# Dividing window into parts (frames,canvas)
canvas = tk.Canvas (master = window, height = 800, width = 1130, background='yellow')
left_frame = tk.Frame (master=window, height =300, width = 350)
left_down_frame= tk.Frame(master=window,height=350,width=350,bg='white')
right_frame = tk.Frame (master=window,height=800,width=50,bg='red')

left_frame.grid (row=1,column=0,sticky='nw') #rowspan=10)
canvas.grid(row=0,column=1,rowspan=10)
left_down_frame.grid(row=9,column=0,sticky='s')
right_frame.grid (row=0, column=2,rowspan=10)

######################################################################################################################################

# Drop down menu for choosing between various graphs

options = ('Graph','Bar Graph', 'Histogram', 'Line Graph', 'Pie Chart')
clicked = tk.StringVar()
clicked.set(options[0])

def choosed (none) :
    choice = clicked.get()              # get the option selected from graph, bargraph,etc
    for widgets in left_frame.winfo_children() :
        widgets.destroy()
    for widgets in left_down_frame.winfo_children() :
        widgets.destroy()
    left_down_frame.config(bg='#F0F0F0')
    graph_left_frame.fun_no = 0
    
    #left_down_frame.config()
    canvas.delete('all')

    if choice == 'Pie Chart' :
        pass
    elif choice == 'Bar Graph' :
        pass
    elif choice == 'Histogram' :
        pass 
    elif choice == 'Line Graph' :
        print('line')
    else :
        #left_down_frame= tk.Frame(master=window,height=350,width=350,bg='white')
        #left_frame.grid (row=1,column=0,sticky='nw')
        graph_left_frame.plot_fun(left_frame)
        keyboard1.keyboard(window,left_down_frame,graph_left_frame.entries)
        graph_canvas_function.raw (canvas,left_frame,graph_left_frame.entries,right_frame)
        
        

# Creating the drop down menu
drop_menu = tk.OptionMenu(window, clicked, *options, command=choosed)
drop_menu.config(width=31,height=2,border=0.5,font=('Times New Roman',15,'normal'))
drop_menu.grid (row=0,column=0,columnspan=2,pady=2,sticky='nw')

#graph_right_frame.right_fun(right_frame)
keyboard1.keyboard(window,left_down_frame,graph_left_frame.entries)
graph_left_frame.plot_fun(left_frame)
graph_canvas_function.raw (canvas,left_frame,graph_left_frame.entries,right_frame)


#print (entries)

window.mainloop()