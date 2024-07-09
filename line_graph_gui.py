from cgitb import text
import tkinter as tk
import line_graph_fun

data = 1                # variable to count no of x,y data inputs
label_entry_list = []   # list of label entries

all_value_entry = ['','','']
total = 3               # variable to count total no of data

#window = tk.Tk()
#window.title ("Graphite")
#window.geometry ('1920x1000')

def Line_Graph (window) :
    left_frame = tk.Frame(master=window,width=351,height=741)
    left_frame.place (x=0,y=59,anchor='nw')

    canvas = tk.Canvas(master=window,width=1165,height=800,bg='white')
    canvas.place(x=355,y=0)

    #right_frame = tk.Frame(master=window,width=50,height=800,bg='blue')
    #right_frame.place(x=1485,y=0)


    value_entry_list_1 = [] # list of value entry for data 1
    value_entry_list_2 = [] # list of value entry for data 2
    value_entry_list_3 = [] # list of value entry for data 2

    # Funtion to create labels
    
    def add_labels () :   # try without passing window as argument
        global data

        # Label for input labels or points
        label = tk.Label(master=left_frame,width=10,height=2,text='Labels',font=('Times New Roman',15,'bold'))
        label.grid (row=0,column=0,sticky='n')

        # Label for value of labels
        value_label = tk.Label(master=left_frame,width=10,height=2,text='Value',font=('Times New Roman',15,'bold'))
        value_label.grid (row=0,column=1,sticky='n',columnspan=3)
        #create_entries()
         
    # Funtion to create entries

    def create_entries () :
        
        global label_entry_list,value_entry_list,data

        # Creating entries

        # Entries for labels
        label_entry = tk.Entry(master=left_frame,width=10,font=('Arial',15,'normal'))
        label_entry.grid (row=data,column=0,sticky='nw',padx=12,pady=5,ipadx=2,ipady=10)
        label_entry_list.append(label_entry)

        # Entries for values
    
        value_entry_1= tk.Entry(master=left_frame,width=5,font=('Arial',15,'normal'))
        value_entry_1.grid (row=data,column=1,columnspan=1,sticky='nw',padx=3,pady=5,ipadx=2,ipady=10)
        value_entry_list_1.append(value_entry_1)
        all_value_entry[0] = value_entry_list_1
            
        if total > 1 :
            value_entry_2=tk.Entry(master=left_frame,width=5,font=('Arial',15,'normal'))
            value_entry_2.grid (row=data,column=2,columnspan=1,sticky='nw',padx=3,pady=5,ipadx=2,ipady=10)
            value_entry_list_2.append(value_entry_2)
            all_value_entry[1] = value_entry_list_2
        
        if total > 2 :
            value_entry_3=tk.Entry(master=left_frame,width=5,font=('Arial',15,'normal'))
            value_entry_3.grid (row=data,column=3,columnspan=1,sticky='nw',padx=3,pady=5,ipadx=2,ipady=10)
            value_entry_list_3.append(value_entry_3)
            all_value_entry[2] = value_entry_list_3

        #print (all_value_entry)
        data+=1

    # Buttons to add more entries

    add_button = tk.Button(master=left_frame,width=7,height=2,text='+',command=lambda:add_fun())
    add_button.grid (row=11,column=3,sticky='e')

    del_button = tk.Button(master=left_frame,width=7,height=2,text='-',command=lambda:del_fun())
    del_button.grid (row=11,column=2,sticky='e')

    # Funtion for this buttons

    def add_fun() :
        global data
        if data < 11 :
            create_entries()
            #data += 1
    
    def del_fun() :
        global data,label_entry_list,value_entry_list
        if data > 2 :
            label_entry_list.pop().destroy()

            value_entry_list_1.pop().destroy()
            all_value_entry[0] = value_entry_list_1

            value_entry_list_2.pop().destroy()
            all_value_entry[1] = value_entry_list_2

            value_entry_list_3.pop().destroy()
            all_value_entry[2] = value_entry_list_3
            
            data -= 1
        
    # Button to draw line graph 

    plot = tk.Button(master=left_frame,text='Draw',width=49,height=3,
                    command=lambda:line_graph_fun.line_graph(canvas,label_entry_list,all_value_entry))
    plot.grid(row=12,column=0,columnspan=4)

    add_labels()
    create_entries()
    window.mainloop()
    ########################################################################################################################    
#Line_Graph(window)