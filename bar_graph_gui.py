import tkinter as tk
import bar_graph_fun



data = 1        # variable to count number of data inputs
label_entry_list = []
value_entry_list = []

# Function to create widgets for Bar Graph

def Bar_Graph (window) :

    ############################################################################################################################

    left_frame = tk.Frame(master=window,width=351,height=741)
    left_frame.place (x=0,y=59,anchor='nw')

    canvas = tk.Canvas(master=window,width=1165,height=800,bg='white')
    canvas.place(x=355,y=0)

    #right_frame = tk.Frame(master=window,width=50,height=800,bg='blue')
    #right_frame.place(x=1485,y=0)

    ########################################################################################################################
    
    # Funtion to create labels
    
    def add_labels () :   # try without passing window as argument
        global data

        # Label for input labels or points
        label = tk.Label(master=left_frame,width=10,height=2,text='Labels',font=('Times New Roman',15,'bold'))
        label.grid (row=0,column=0,sticky='n')

        # Label for value of labels
        value_label = tk.Label(master=left_frame,width=10,height=2,text='Value',font=('Times New Roman',15,'bold'))
        value_label.grid (row=0,column=1,sticky='n')

        create_entries()
         
    # Funtion to create entries

    def create_entries () :
        
        global label_entry_list,value_entry_list,data

        # Creating entries

        # Entries for labels
        label_entry = tk.Entry(master=left_frame,width=15,font=('Arial',15,'normal'))
        label_entry.grid (row=data,column=0,sticky='nw',padx=2,pady=5,ipadx=2,ipady=10)
        label_entry_list.append(label_entry)

        # Entries for values
        value_entry = tk.Entry(master=left_frame,width=15,font=('Arial',15,'normal'))
        value_entry.grid (row=data,column=1,columnspan=2,sticky='nw',padx=2,pady=5,ipadx=2,ipady=10)
        value_entry_list.append(value_entry)
            
        data+=1
    ########################################################################################################################    

    # Buttons to add more entries

    add_button = tk.Button(master=left_frame,width=5,height=2,text='+',command=lambda:add_fun())
    add_button.grid (row=11,column=2,sticky='e')

    del_button = tk.Button(master=left_frame,width=5,height=2,text='-',command=lambda:del_fun())
    del_button.grid (row=11,column=1,sticky='e')

    # Funtion for this buttons

    def add_fun() :
        global data
        if data < 11 :
            create_entries()
            #data += 1
    
    def del_fun() :
        global data,label_entry_list,value_entry_list
        if data > 1 :
            label_entry_list.pop().destroy()
            value_entry_list.pop().destroy()
            data -= 1

    # Button to draw bar graph

    plot = tk.Button(master=left_frame,text='Draw',width=49,height=3,
                     command=lambda:bar_graph_fun.bar_graph(canvas,label_entry_list,value_entry_list))
    plot.grid(row=12,column=0,columnspan=4)
    
    add_labels()
    
    '''try :
        bar_graph_fun.bar_graph(canvas,label_entry_list,value_entry_list)
    except :
        pass'''
    window.mainloop()




#Bar_Graph(window)