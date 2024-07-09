import tkinter as tk

fun_no = 0
entries = []
color = ['red','green','yellow','blue','orange']
labels = []
def fun_input (left_frame) :
    global fun_no
    print (fun_no)
    if fun_no > 4 :
            pass 
    else :
        entry = tk.Entry(master=left_frame, width=32,font=('consolas',12,'normal'))
        #entry.insert(0,'2*x')
        entry.grid(row=fun_no, column=1,pady=5,ipady=8,sticky='nw',columnspan=2)
        #entry_text.append("")
        entry.focus_set()
        entries.append (entry)

        label = tk.Label(master=left_frame,width=5,border=0.5,text='F'+str(fun_no+1),bg=color[fun_no])
        label.grid(row=fun_no,column=0,pady=5,ipady=8,sticky='nw')
        labels.append (label)
        fun_no += 1
        print (entries)

#def abc(left_frame) :
#
#    for i in range (2) :
#        label = tk.Label(master=left_frame,width=5,border=0.5,text='F'+str(i+1))
#        label.grid(row=i,column=0,pady=5,ipady=8,sticky='nw')
#
#        entry = tk.Entry(master=left_frame, width=32, font=('calibre',12,'normal'))
#        entry.grid(row=i, column=1,pady=5,ipady=8,sticky='nw')
#        #entry.focus()
#    
#    def test () :
#        entry_no = left_frame.focus_get()
#        entry_no.insert(0,'A')
#        #print (a)

#def add_fun (left_frame) :
#    pass


def del_fun() :
    '''Function to delete functions entry box'''
    global fun_no
    if fun_no > 1 :
        entries.pop().destroy() 
        entries[-1].focus_set()
        labels.pop().destroy()
        #entry_text[-1] = ""
        fun_no-=1
    else :
        pass
    


def plot_fun (left_frame) :
    add = tk.Button(master=left_frame,text='+',width=7,height=3,border=0.5,command=lambda:fun_input(left_frame))    
    add.grid(row=5,column=1,sticky='e',pady=2)

    del_button = tk.Button(master=left_frame,text='-',width=7,height=3,border=0.5,command=lambda:del_fun())    
    del_button.grid(row=5,column=0,sticky='e',pady=2)

    fun_input(left_frame)

    




#fun_input(left_frame)

