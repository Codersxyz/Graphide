from operator import le
import tkinter as tk
from tkinter.font import NORMAL
import graph_gui
#from gui complete.graph_gui import graph_gui
#from GUI.graph_left_frame import abc
#import graph_canvas_function
#import graph_left_frame
#import keyboard1
import pie_chart_gui
import bar_graph_gui
import line_graph_gui
import histogram_gui
#import graph_right_frame


# Creating the Main Window
window = tk.Tk()
window.title ("Graphite")
window.geometry ('1920x1000')

'''
# Dividing window into parts (frames,canvas)
canvas = tk.Canvas (master = window, height = 800, width = 1130, background='yellow')
left_frame = tk.Frame (master=window, height =300, width = 350)
left_down_frame= tk.Frame(master=window,height=350,width=350,bg='white')
right_frame = tk.Frame (master=window,height=800,width=50,bg='red')

left_frame.grid (row=1,column=0,sticky='nw') #rowspan=10)
canvas.grid(row=0,column=1,rowspan=10)
left_down_frame.grid(row=9,column=0,sticky='s')
right_frame.grid (row=0, column=2,rowspan=10)
'''
######################################################################################################################################

# Drop down menu for choosing between various graphs

options = ('Graph','Bar Graph', 'Histogram', 'Line Graph', 'Pie Chart')
clicked = tk.StringVar()
clicked.set(options[0])

def choosed (none) :
    choice = clicked.get()              # get the option selected from graph, bargraph,etc
    try :
        for widgets in window.winfo_children() :
            if widgets != drop_menu :
                widgets.destroy()
       # left_frame.destroy()
       # right_frame.destroy()
       # canvas.destroy()
       # left_down_frame.destroy()
    except :
        pass

    #for widgets in left_down_frame.winfo_children() :
    #    widgets.destroy()
    #left_down_frame.config(bg='#F0F0F0')
    #graph_left_frame.fun_no = 0
    
    #left_down_frame.config()
    #canvas.delete('all')

    #window.destroy()
    if choice == 'Pie Chart' :
        # resetting variable to default
        pie_chart_gui.data = 1
        pie_chart_gui.label_entry_list = []
        pie_chart_gui.value_entry_list = []
        pie_chart_gui.pie_chart_gui(window)
    elif choice == 'Bar Graph' :
        # resetting variables to default
        bar_graph_gui.data = 1
        bar_graph_gui.label_entry_list = []
        bar_graph_gui.value_entry_list = []
        bar_graph_gui.Bar_Graph(window)
    elif choice == 'Histogram' :
        histogram_gui.Histogram(window)
    elif choice == 'Line Graph' :
        line_graph_gui.all_value_entry = ['','','']
        line_graph_gui.data = 1
        line_graph_gui.label_entry_list = []
        line_graph_gui.Line_Graph(window)
    else :
        '''
        #left_down_frame= tk.Frame(master=window,height=350,width=350,bg='white')
        #left_frame.grid (row=1,column=0,sticky='nw')
        graph_left_frame.plot_fun(left_frame)
        keyboard1.keyboard(window,left_down_frame,graph_left_frame.entries)
        graph_canvas_function.raw (canvas,left_frame,graph_left_frame.entries,right_frame)
        '''
        graph_gui.graph_gui(window)
        

# Creating the drop down menu
drop_menu = tk.OptionMenu(window, clicked, *options, command=choosed)
drop_menu.config(width=31,height=2,border=0.5,font=('Times New Roman',15,'normal'))
drop_menu.grid (row=0,column=0,columnspan=2,pady=2,sticky='nw')

'''
#graph_right_frame.right_fun(right_frame)
keyboard1.keyboard(window,left_down_frame,graph_left_frame.entries)
graph_left_frame.plot_fun(left_frame)
graph_canvas_function.raw (canvas,left_frame,graph_left_frame.entries,right_frame)
'''

#print (entries)
graph_gui.graph_gui(window)

window.mainloop()