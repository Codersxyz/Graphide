from ast import Set
from sqlite3 import Row
import tkinter as tk
from tkinter.font import BOLD, NORMAL
from turtle import width
#from graph_left_frame import *

# Creating the Main Window
window = tk.Tk()
window.title ("Graphite")
window.geometry ('1920x1000')


canvas = tk.Canvas (master = window, height = 800, width = 1130, background='yellow')

left_frame = tk.Frame (master=window, height =400, width = 350)
left_down_frame= tk.Frame(master=window,height=400,width=350,bg='green')
#top_left_frame = tk.Frame (master=window,height=50,width=350,bg='green')
right_frame = tk.Frame (master=window,height=800,width=50,bg='red')
#canvas2 = tk.Canvas (master = window, height = 800, width = 300, background='red')

left_frame.grid (row=1,column=0,sticky='nw',rowspan=5) #rowspan=10)
canvas.grid(row=0,column=10,rowspan=10)
left_down_frame.grid(row=9,column=0)
#top_left_frame.grid (row=0,column=0,sticky='nw')#rowspan=2,columnspan=10)
right_frame.grid (row=0, column=11,rowspan=10)
#label = tk.Label(master=top_left_frame, text="Graph")
#label.grid (row=0,column=0)
#top_left_frame.grid (row=0,column=0)

#canvas1.grid (row = 0, column = 0)
#canvas2.grid (row = 0, column = 2)


#b1 = tk.Button(master = top_left_frame,height=2,width = 49, border=0.5)
#b1.pack()
#b2 = tk.Button(master = canvas1, height = 10, width = 10)
#b2.grid (row=0,column=1)
window.update()


# Drop down menu for choosing between various graphs

options = ('Graph','Bar Graph', 'Histrogram', 'Line Graph', 'Pie Chart')
clicked = tk.StringVar()
clicked.set(options[0])

def choosed (choice) :
    choice = clicked.get ()
    #print (choice)

# Creating the drop down menu
drop_menu = tk.OptionMenu(window, clicked, *options, command= choosed)
drop_menu.config(width=31,height=2,border=0.5,font=('Times New Roman',15,'normal'))
drop_menu.grid (row=0,column=0,columnspan=2,sticky='nw')

# Input boxes 

fun_no = 1
def fun_input () :
    global fun_no
    if fun_no > 10 :
            pass 
    else :
        fun_no += 1
        for i in range (fun_no) :
            print (fun_no)
            entry = tk.Entry(master=left_frame, width=32, font=('calibre',12,'normal'))
            entry.grid(row=fun_no-1, column=1,pady=5,ipady=8,sticky='nw')
            label = tk.Label(master=left_frame,width=5,border=0.5,text='F'+str(fun_no-1))
            label.grid(row=fun_no-1,column=0,pady=5,ipady=8,sticky='nw')

plot = tk.Button(master=left_frame,text='Plot',width=49,height=3,border=0.5,command=fun_input)    
plot.grid(row=5,column=0,columnspan=2,sticky='s',pady=2)
#fun_input()
colors = ('red','blue')




'''
def fun_input () :
    global fun_no
    if fun_no == 10 :
        pass 
    else :
        fun_no += 1
        exec ('f'+str(fun_no)+"= tk.Entry(left_frame, width=32, font=('calibre',12,'normal'))\n"
          'label_'+str(fun_no)+"=tk.Label(left_frame, width=5,border=0.5,text='F'+str(fun_no))\n"
          'label_'+str(fun_no)+".grid(row=fun_no,column=0,pady=5,ipady=8,sticky='w')\n"
          'f'+str(fun_no)+".grid(row=fun_no, column=1,pady=5,ipady=8,sticky='w')") 

def fun_input () :
    global fun_no
    if fun_no > 10 :
        pass 
    else :
        fun_no += 1
        for i in range (fun_no) :
            entry = tk.Entry(left_frame, width=32, font=('calibre',12,'normal'))
            entry.grid(row=fun_no-1, column=1,pady=5,ipady=8,sticky='w')
            label = tk.Label(left_frame,width=5,border=0.5,text='F'+str(fun_no-1))
            label.grid(row=fun_no-1,column=0,pady=5,ipady=8,sticky='w')
        

#f1 = tk.Entry(left_frame, width=31, font=('calibre',15,'normal'))
#f1.grid (row=2,column=0,sticky='nw')


fun_input()

# Function to plot and add new function
plot = tk.Button(left_frame,text='Plot',width=49,height=2,border=0.5,command=fun_input)
plot.grid(row=11,column=0,columnspan=2,sticky='s')

# Numpad 



'''


#for i in range (fun_no) :
#f1.pack ()
window.mainloop ()