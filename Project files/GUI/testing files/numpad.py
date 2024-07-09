from logging import root
import tkinter as tk
from tkinter.font import NORMAL
from tkinter.ttk import Combobox, Label

window = tk.Tk()
window.geometry('800x1000')
window.config(bg='black')
'''
top = tk.Toplevel(window)
top.geometry('800x1000')
top.title('Graphite')
'''
numpad = tk.Frame(master=window,width=350,height=400)
left_frame = tk.Frame (master=window, height =400, width = 350,bg='green')
numpad.grid (row=1)

left_down_frame= tk.Frame(master=window,height=400,width=350)
left_down_frame.grid(row=1,column=0)
left_frame.grid(row=0,column=0)


k = 1
for i in reversed (range (3)) :
    for j in range (3) :
        def display (num = k) :
            print (num)
        nums = tk.Button(master=left_down_frame,width=8,height=2,text=str(k),
                        font=('consolas',12,NORMAL),command=display,border=0.5,bg='#ffffff')
        nums.grid(row=i+4,column=j,padx=2,pady=2)
        k+=1

arith_button = (chr(247),chr(215),'-','+')
row_2_button = ('(',')','x','y')

# 0
nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,NORMAL),
                text=str(0),border=0.5,command=lambda:display(0),bg='#ffffff')
nums.grid(row=7,column=0,padx=1,pady=1)


# Decimal Point
nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                text='.',border=0.5,command=lambda:display('.'),bg='#d5d5d5')
nums.grid(row=7,column=1,padx=1,pady=1)

#Equals to
nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                text='=',border=0.5,command=lambda:display('='),bg='#d5d5d5')
nums.grid(row=7,column=2,padx=1,pady=1)


for i in range (4) :
    def display (num = arith_button[i]) :
        print (num)
    nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                text=arith_button[i],border=0.5,command=display,bg='#d5d5d5')
    nums.grid(row=i+4,column=3,padx=1,pady=1)


for i in range (4) :
    def display (num = row_2_button[i]) :
        print (num)
    nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                text=row_2_button[i],border=0.5,command=display,bg='#d5d5d5')
    nums.grid(row=3,column=i,padx=1,pady=1)

# Power
nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                text='^',border=0.5,command=lambda:display('^'),bg='#d5d5d5')
nums.grid(row=1,column=1,padx=1,pady=1)

# Log 
nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                text='log',border=0.5,command=lambda:display('log('),bg='#d5d5d5')
nums.grid(row=1,column=2,padx=1,pady=1)

# All Clear
nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'bold'),
                text='AC',border=0.5,command=lambda:display('AC'),bg='#d5d5d5')
nums.grid(row=1,column=0,padx=1,pady=1)

# Clear 
nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                text='Clear',border=0.5,command=lambda:display('Clear'),bg='#d5d5d5')
nums.grid(row=1,column=3,padx=1,pady=1)

# Row 1 
row_1_buttons = (chr(960),'e',chr(8730),'INV',)

for i in range (4) :
    nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                text=row_1_buttons[i],border=0.5,command=lambda:display(row_1_buttons[i]),bg='#d5d5d5')
    nums.grid(row=1,column=i,padx=1,pady=1)


# Trignometric functions

trig = tk.StringVar()
trig.set('Trignometric')
def trig_fun (x) : 
    trig.set('Trignometric')
trig_options = ('sin','cos','tan','sec','cosec','cot')
trig_menu = tk.OptionMenu(left_down_frame,trig,*trig_options,command=trig_fun)
trig_menu.config(width=12,height=2,border=0,font=('consolas',12,'normal'))
trig_menu.grid(row=0,column=0,padx=1,pady=2,columnspan=2,sticky='nw')


a = Combobox
'''
# Division
nums= tk.Button(master=left_down_frame,width=8,height=3,font=('Times New Roman',12,'bold'),
                text=chr(247),border=0.5,command=lambda:display(chr(247)),bg='#d5d5d5')
nums.grid(row=0,column=4,padx=1,pady=1)

# Multiplication
nums= tk.Button(master=left_down_frame,width=8,height=3,font=('Times New Roman',12,'bold'),
                text=chr(215),border=0.5,command=lambda:display('*'),bg='#d5d5d5')
nums.grid(row=1,column=4,padx=1,pady=1)

# Subtraction
nums= tk.Button(master=left_down_frame,width=8,height=3,font=('Times New Roman',12,'bold'),
                text='-',border=0.5,command=lambda:display('-'),bg='#d5d5d5')
nums.grid(row=2,column=4,padx=1,pady=1)

# Addition
nums= tk.Button(master=left_down_frame,width=8,height=3,font=('Times New Roman',12,'bold'),
                text='+',border=0.5,command=lambda:display('+'),bg='#d5d5d5')
nums.grid(row=3,column=4,padx=1,pady=1)
'''


print (type(nums)) 

window.mainloop()
